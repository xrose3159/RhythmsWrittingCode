/**
 * 表单验证工具
 * 提供常用的表单验证功能
 */

/**
 * 验证规则集合
 */
export const rules = {
  /**
   * 必填项验证
   * @param {string} message - 错误提示信息
   * @returns {Object} 验证规则对象
   */
  required: (message = '此字段不能为空') => ({
    required: true,
    message
  }),

  /**
   * 邮箱格式验证
   * @param {string} message - 错误提示信息
   * @returns {Object} 验证规则对象
   */
  email: (message = '请输入有效的邮箱地址') => ({
    type: 'email',
    message
  }),

  /**
   * 手机号验证（中国大陆）
   * @param {string} message - 错误提示信息
   * @returns {Object} 验证规则对象
   */
  phone: (message = '请输入有效的手机号码') => ({
    pattern: /^1[3-9]\d{9}$/,
    message
  }),

  /**
   * URL格式验证
   * @param {string} message - 错误提示信息
   * @returns {Object} 验证规则对象
   */
  url: (message = '请输入有效的URL地址') => ({
    type: 'url',
    message
  }),

  /**
   * 字符串长度验证
   * @param {number} min - 最小长度
   * @param {number} max - 最大长度
   * @param {string} message - 错误提示信息
   * @returns {Object} 验证规则对象
   */
  length: (min, max, message) => ({
    min,
    max,
    message: message || `长度必须在${min}到${max}个字符之间`
  }),

  /**
   * 数字范围验证
   * @param {number} min - 最小值
   * @param {number} max - 最大值
   * @param {string} message - 错误提示信息
   * @returns {Object} 验证规则对象
   */
  range: (min, max, message) => ({
    type: 'number',
    min,
    max,
    message: message || `数值必须在${min}到${max}之间`
  }),

  /**
   * 密码强度验证
   * @param {string} message - 错误提示信息
   * @returns {Object} 验证规则对象
   */
  password: (message = '密码必须包含字母、数字和特殊字符，长度至少为8位') => ({
    pattern: /^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$/,
    message
  }),

  /**
   * 确认密码验证
   * @param {Function} getFieldValue - 获取表单字段值的函数
   * @param {string} fieldName - 密码字段名
   * @param {string} message - 错误提示信息
   * @returns {Object} 验证规则对象
   */
  confirmPassword: (getFieldValue, fieldName = 'password', message = '两次输入的密码不一致') => ({
    validator: (_, value) => {
      if (!value || getFieldValue(fieldName) === value) {
        return Promise.resolve();
      }
      return Promise.reject(new Error(message));
    }
  }),

  /**
   * 中文字符验证
   * @param {string} message - 错误提示信息
   * @returns {Object} 验证规则对象
   */
  chinese: (message = '请输入中文字符') => ({
    pattern: /^[\u4e00-\u9fa5]+$/,
    message
  }),

  /**
   * 身份证号验证
   * @param {string} message - 错误提示信息
   * @returns {Object} 验证规则对象
   */
  idCard: (message = '请输入有效的身份证号码') => ({
    pattern: /(^\d{15}$)|(^\d{18}$)|(^\d{17}(\d|X|x)$)/,
    message
  }),

  /**
   * 自定义正则验证
   * @param {RegExp} pattern - 正则表达式
   * @param {string} message - 错误提示信息
   * @returns {Object} 验证规则对象
   */
  pattern: (pattern, message = '格式不正确') => ({
    pattern,
    message
  }),

  /**
   * 自定义验证器
   * @param {Function} validator - 验证函数
   * @param {string} message - 错误提示信息
   * @returns {Object} 验证规则对象
   */
  custom: (validator, message = '验证失败') => ({
    validator: (_, value) => {
      if (validator(value)) {
        return Promise.resolve();
      }
      return Promise.reject(new Error(message));
    }
  })
};

/**
 * 创建表单验证规则
 * @param {Object} fieldRules - 字段验证规则配置
 * @returns {Object} 表单验证规则对象
 */
export const createFormRules = (fieldRules) => {
  const formRules = {};
  
  Object.keys(fieldRules).forEach(field => {
    formRules[field] = Array.isArray(fieldRules[field]) 
      ? fieldRules[field] 
      : [fieldRules[field]];
  });
  
  return formRules;
};

/**
 * 常用表单验证规则组合
 */
export const commonRules = {
  // 用户名验证规则
  username: [
    rules.required('请输入用户名'),
    rules.length(3, 20, '用户名长度必须在3-20个字符之间'),
    rules.pattern(/^[a-zA-Z0-9_-]+$/, '用户名只能包含字母、数字、下划线和连字符')
  ],
  
  // 密码验证规则
  password: [
    rules.required('请输入密码'),
    rules.length(8, 20, '密码长度必须在8-20个字符之间'),
    rules.pattern(/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$/, '密码必须包含大小写字母和数字')
  ],
  
  // 邮箱验证规则
  email: [
    rules.required('请输入邮箱'),
    rules.email('请输入有效的邮箱地址')
  ],
  
  // 手机号验证规则
  phone: [
    rules.required('请输入手机号'),
    rules.phone('请输入有效的手机号码')
  ]
};

/**
 * 表单验证工具
 */
export default {
  rules,
  createFormRules,
  commonRules
};