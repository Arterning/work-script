#!/bin/bash
###
 # @Author: ning.huang ning.huang
 # @Date: 2022-11-15 13:42:48
 # @LastEditors: ning.huang ning.huang
 # @LastEditTime: 2022-11-15 13:47:35
 # @FilePath: \code\linux\install-env\install.sh
 # @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
### 

# install nvm
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.2/install.sh | bash
source ~/.bashrc


nvm install --lts