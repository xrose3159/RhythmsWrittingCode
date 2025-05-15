#!/bin/bash

# 创建项目基本目录结构

# 前端目录
mkdir -p frontend/src/{components,pages,assets,utils,styles}
mkdir -p frontend/public

# 后端目录
mkdir -p backend/{api,services,models,utils,config}

# AI模型目录
mkdir -p ai_model/{training,inference,data,models,evaluation}

# 创建基本配置文件
touch frontend/package.json
touch frontend/vite.config.js
touch frontend/.gitignore

touch backend/requirements.txt
touch backend/app.py
touch backend/.gitignore

touch ai_model/requirements.txt
touch ai_model/README.md

# 创建主项目配置文件
touch .gitignore
touch docker-compose.yml

echo "项目目录结构创建完成！"