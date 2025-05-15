/**
 * API接口封装
 * 用于前端与后端服务的交互
 */

import axios from 'axios';

// 创建axios实例
const api = axios.create({
  baseURL: '/api',
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json'
  }
});

// 请求拦截器
api.interceptors.request.use(
  config => {
    // 可以在这里添加认证信息，如token
    const token = localStorage.getItem('token');
    if (token) {
      config.headers['Authorization'] = `Bearer ${token}`;
    }
    return config;
  },
  error => {
    return Promise.reject(error);
  }
);

// 响应拦截器
api.interceptors.response.use(
  response => {
    return response.data;
  },
  error => {
    // 统一处理错误
    if (error.response) {
      // 服务器返回错误信息
      const { status, data } = error.response;
      if (status === 401) {
        // 未授权，可以在这里处理登出逻辑
        localStorage.removeItem('token');
        window.location.href = '/login';
      }
      return Promise.reject(data || '服务器错误');
    } else if (error.request) {
      // 请求发出但没有收到响应
      return Promise.reject('网络错误，请检查您的网络连接');
    } else {
      // 请求配置出错
      return Promise.reject('请求配置错误');
    }
  }
);

// API接口
const apiService = {
  // 用户相关
  user: {
    login: (data) => api.post('/user/login', data),
    register: (data) => api.post('/user/register', data),
    getProfile: () => api.get('/user/profile'),
    updateProfile: (data) => api.put('/user/profile', data)
  },
  
  // 字体创作相关
  font: {
    create: (data) => api.post('/font/create', data),
    getList: (params) => api.get('/font/list', { params }),
    getDetail: (id) => api.get(`/font/detail/${id}`),
    update: (id, data) => api.put(`/font/${id}`, data),
    delete: (id) => api.delete(`/font/${id}`),
    // 上传字体图片
    uploadImage: (formData) => api.post('/font/upload', formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    })
  },
  
  // 样式转换相关
  styleTransfer: {
    // 获取可用的样式列表
    getStyles: () => api.get('/style/list'),
    // 执行样式转换
    transfer: (data) => api.post('/style/transfer', data),
    // 获取转换历史
    getHistory: (params) => api.get('/style/history', { params }),
    // 获取转换结果详情
    getResult: (id) => api.get(`/style/result/${id}`)
  }
};

export default apiService;