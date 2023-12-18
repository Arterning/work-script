# asr_client.py
# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# NOTICE: pip3 install websocket-client
# --url wss://lm_experience.sensetime.com/v2/asr/non-streaming --wav_path D:\download\001.wav --streaming
# --url wss://localhost/v2/asr/non-streaming --wav_path D:\download\001.wav --streaming
import threading
import _thread
import argparse
import websocket
import datetime
import json
import wave
import time
import sys
import ssl
import os


class WebsocketClient():

    def __init__(self, host, port, wav_path, log_path):
        self.host = host
        self.port = port
        self.wav_path = wav_path
        self.log_path = log_path
        self.file_name, _ = os.path.splitext(os.path.basename(self.wav_path))
        self.start = 0

    def file_write(self, now_time, msg):
        if self.log_path != '':
            with open(self.log_path, 'a') as file:
                # file.write(self.file_name)
                # file.write('\t')
                # file.write(now_time)
                # file.write('\t')
                file.write(msg)
                file.write('\n')

    def on_message(self, ws, message):
        msg = json.loads(message)
        print(msg)
        if msg['status'] == 'ok':
            if msg['type'] == 'partial_result':
                result = msg['result']
                # print(result, file=sys.stderr, flush=True)
            if msg['type'] == 'final_result':
                # print(message)
                result = msg['result']
                if self.start != 0:
                    end = datetime.datetime.now()
                    with open("time.log", 'a') as f:
                        f.write(str((end - self.start).microseconds))
                        f.write('\n')
                    print((end - self.start).microseconds)
                    self.start = 0
                    print(end.strftime('%Y-%m-%d %H:%M:%S.%f'))
                self.file_write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'), result)
                print(result, file=sys.stderr, flush=True)
            if msg['type'] == 'speech_end':
                print('receive speech end', file=sys.stderr, flush=True)
                self.ws.close()
        else:
            print(msg['message'], file=sys.stderr, flush=True)
            self.ws.close()

    def on_error(self, ws, error):
        print(error, file=sys.stderr, flush=True)
        self.ws.close()

    def on_close(self, ws, close_status_code, close_msg):
        print("### closed ###")
        self.ws.close()

    def on_open(self, ws):
        def run(*args):
            try:
                if self.audio_type == 'wav':
                    with wave.open(self.wav_path, 'rb') as reader:
                        n = reader.getnframes()
                        chunk = self.millseconds * reader.getframerate() // 1000
                        # print("framerate:", reader.getframerate())
                        # print("chunk:", chunk)
                        n = n // chunk
                        # print(n)
                        if (n % chunk) != 0:
                            n += 1
                        self.send_start_signal()
                        for i in range(n):
                            # if i in self.frame_nums:
                            #    self.start = datetime.datetime.now()
                            #    print("idx:%d, time:%s\n"%(i, self.start.strftime('%Y-%m-%d %H:%M:%S.%f')))
                            frame = reader.readframes(chunk)
                            self.send_data(frame)
                            # print("send data size: ", len(frame))
                            if self.streaming:
                                time.sleep(self.millseconds / 1000)
                        self.send_end_signal()
                else:
                    with open(self.wav_path, 'rb') as file:
                        chunk = 2 * self.millseconds * self.sample_rate // 1000
                        # print("chunk:", chunk)
                        self.send_start_signal()
                        while True:
                            frame = file.read(chunk)
                            if not frame:
                                break
                            self.send_data(frame)
                            # print("send data size: ", len(frame))
                            if self.streaming:
                                time.sleep(self.millseconds / 1000)
                        self.send_end_signal()
                print("send finish")
            except:
                print("Unexpected error:", sys.exc_info()[0])

        _thread.start_new_thread(run, ())

    def run(self):
        if self.url:
            url = self.url
        else:
            url = 'ws://' + self.host + ':' + self.port + '/'
        self.ws = websocket.WebSocketApp(url,
                                         {'Authorization': '1dd04d5de3cf467087a24ed77814ec9e'},
                                         on_open=self.on_open,
                                         on_message=self.on_message,
                                         on_error=self.on_error,
                                         on_close=self.on_close)
        self.ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})

    def send_start_signal(self):
        message = json.dumps({'signal': 'start', 'continuous_decoding': self.continuous_decoding,
                              'speech_pause_time': self.speech_pause_time, 'server_vad': self.server_vad,
                              'punctuation': self.punctuation, 'tradition': self.tradition,
                              'product_id': self.pid, 'app_id': self.appid, 'device_id': self.devid,
                              'mic_volume': 0.8, 'store': self.store})
        self.ws.send(message)

    def send_end_signal(self):
        message = json.dumps({'signal': 'end'})
        self.ws.send(message)
        print('send end message')

    def send_data(self, binary):
        self.ws.send(binary, websocket.ABNF.OPCODE_BINARY)

    def set_chunk_size(self, millseconds):
        self.millseconds = millseconds

    def set_speech_pause_time(self, time):
        self.speech_pause_time = time

    def set_sample_rate(self, sample_rate):
        self.sample_rate = sample_rate

    def set_audio_type(self, audio_type):
        self.audio_type = audio_type

    def set_continuous_decoding(self, continuous_decoding):
        self.continuous_decoding = continuous_decoding

    def set_server_vad(self, server_vad):
        self.server_vad = server_vad

    def set_punctuation(self, punctuation):
        self.punctuation = punctuation

    def set_streaming(self, streaming):
        self.streaming = streaming

    def set_tradition(self, tradition):
        self.tradition = tradition

    def set_url(self, url):
        self.url = url

    def set_id(self, pid, appid, devid):
        self.pid = pid
        self.appid = appid
        self.devid = devid

    def set_store(self, store):
        self.store = store


parser = argparse.ArgumentParser()
parser.add_argument('--url', help='remote server url', type=str, default="")
# parser.add_argument('--host', help='remote host', type=str, default="14.215.130.140")
parser.add_argument('--host', help='remote host', type=str, default="127.0.0.1")
parser.add_argument('--port', help='remote port', type=str, default="10086")
parser.add_argument('-w', '--wav_path', required=True, help='wave path', type=str)
parser.add_argument('--log_path', help='log_path', type=str, default='')
parser.add_argument('--chunk_millseconds', help='send millseconds audio', type=int, default=40)
parser.add_argument('--speech_pause_time', help='set speech pause time', type=int, default=300)
parser.add_argument('--sample_rate', help='set speech sample rate', type=int, default=16000)
parser.add_argument('--audio_type', help='set speech audio type, default set wav', type=str, default='wav')
parser.add_argument('--continuous_decoding', action='store_true',
                    help='continue to do next recognition otherwise stop recognition')
parser.add_argument('--server_vad', action='store_true', help='use server vad to split audio')
parser.add_argument('--punctuation', help='use punctuation', type=int, default=0)
parser.add_argument('--streaming', action='store_true', help='streaming send audio')
parser.add_argument('--tradition', action='store_true', help='response traditon chinese')
parser.add_argument('--store', action='store_true', help='store asr message and audio')
parser.add_argument('--product_id', help='product id', type=str, default='test')
parser.add_argument('--app_id', help='app id', type=str, default='test')
parser.add_argument('--device_id', help='device id', type=str, default='test')


def main():
    args = parser.parse_args()
    if not os.path.exists(args.wav_path):
        print(args.wav_path, "is not exists")
        return
    wc = WebsocketClient(args.host, args.port, args.wav_path, args.log_path)
    wc.set_chunk_size(args.chunk_millseconds)
    wc.set_speech_pause_time(args.speech_pause_time)
    wc.set_sample_rate(args.sample_rate)
    wc.set_audio_type(args.audio_type)
    wc.set_continuous_decoding(args.continuous_decoding)
    wc.set_server_vad(args.server_vad)
    wc.set_punctuation(args.punctuation)
    wc.set_streaming(args.streaming)
    wc.set_tradition(args.tradition)
    wc.set_url(args.url)
    wc.set_id(args.product_id, args.app_id, args.device_id)
    wc.set_store(args.store)
    wc.run()


if __name__ == '__main__':
    main()
