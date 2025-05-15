/**
 * 存储工具
 * 用于处理本地存储操作
 */

/**
 * 本地存储服务
 */
const storageService = {
  /**
   * 设置本地存储项
   * @param {string} key - 存储键名
   * @param {any} value - 存储值
   * @param {boolean} useSession - 是否使用会话存储，默认为false（使用localStorage）
   */
  set: (key, value, useSession = false) => {
    try {
      const storage = useSession ? sessionStorage : localStorage;
      const stringValue = typeof value === 'object' ? JSON.stringify(value) : String(value);
      storage.setItem(key, stringValue);
    } catch (error) {
      console.error('存储数据失败:', error);
    }
  },

  /**
   * 获取本地存储项
   * @param {string} key - 存储键名
   * @param {boolean} useSession - 是否使用会话存储，默认为false（使用localStorage）
   * @param {boolean} parseJson - 是否解析JSON，默认为true
   * @returns {any} 存储值
   */
  get: (key, useSession = false, parseJson = true) => {
    try {
      const storage = useSession ? sessionStorage : localStorage;
      const value = storage.getItem(key);
      
      if (value === null) {
        return null;
      }
      
      if (parseJson) {
        try {
          return JSON.parse(value);
        } catch (e) {
          // 如果不是有效的JSON，则返回原始值
          return value;
        }
      }
      
      return value;
    } catch (error) {
      console.error('获取存储数据失败:', error);
      return null;
    }
  },

  /**
   * 移除本地存储项
   * @param {string} key - 存储键名
   * @param {boolean} useSession - 是否使用会话存储，默认为false（使用localStorage）
   */
  remove: (key, useSession = false) => {
    try {
      const storage = useSession ? sessionStorage : localStorage;
      storage.removeItem(key);
    } catch (error) {
      console.error('移除存储数据失败:', error);
    }
  },

  /**
   * 清空所有本地存储
   * @param {boolean} useSession - 是否使用会话存储，默认为false（使用localStorage）
   */
  clear: (useSession = false) => {
    try {
      const storage = useSession ? sessionStorage : localStorage;
      storage.clear();
    } catch (error) {
      console.error('清空存储数据失败:', error);
    }
  },

  /**
   * 获取所有存储键名
   * @param {boolean} useSession - 是否使用会话存储，默认为false（使用localStorage）
   * @returns {string[]} 键名数组
   */
  keys: (useSession = false) => {
    try {
      const storage = useSession ? sessionStorage : localStorage;
      return Object.keys(storage);
    } catch (error) {
      console.error('获取存储键名失败:', error);
      return [];
    }
  },

  /**
   * 检查存储项是否存在
   * @param {string} key - 存储键名
   * @param {boolean} useSession - 是否使用会话存储，默认为false（使用localStorage）
   * @returns {boolean} 是否存在
   */
  has: (key, useSession = false) => {
    try {
      const storage = useSession ? sessionStorage : localStorage;
      return storage.getItem(key) !== null;
    } catch (error) {
      console.error('检查存储项失败:', error);
      return false;
    }
  },

  /**
   * 获取存储项数量
   * @param {boolean} useSession - 是否使用会话存储，默认为false（使用localStorage）
   * @returns {number} 存储项数量
   */
  size: (useSession = false) => {
    try {
      const storage = useSession ? sessionStorage : localStorage;
      return storage.length;
    } catch (error) {
      console.error('获取存储大小失败:', error);
      return 0;
    }
  }
};

export default storageService;