import React from 'react'
import { Menu } from 'antd'
import { Link, useLocation } from 'react-router-dom'
import {
  HomeOutlined,
  EditOutlined,
  EyeOutlined,
  SwapOutlined,
  HistoryOutlined,
  StarOutlined,
  SettingOutlined
} from '@ant-design/icons'
import '../styles/components/MainSidebar.css'

const MainSidebar = () => {
  const location = useLocation()
  
  const menuItems = [
    {
      key: '/',
      icon: <HomeOutlined />,
      label: <Link to="/">首页</Link>,
    },
    {
      key: '/create',
      icon: <EditOutlined />,
      label: <Link to="/create">字体创作</Link>,
    },
    {
      key: '/preview',
      icon: <EyeOutlined />,
      label: <Link to="/preview">字体预览</Link>,
    },
    {
      key: '/transfer',
      icon: <SwapOutlined />,
      label: <Link to="/transfer">风格迁移</Link>,
    },
    {
      key: '/history',
      icon: <HistoryOutlined />,
      label: <Link to="/history">创作历史</Link>,
    },
    {
      key: '/favorites',
      icon: <StarOutlined />,
      label: <Link to="/favorites">收藏作品</Link>,
    },
    {
      key: '/settings',
      icon: <SettingOutlined />,
      label: <Link to="/settings">系统设置</Link>,
    },
  ]

  return (
    <div className="main-sidebar">
      <Menu
        mode="inline"
        selectedKeys={[location.pathname]}
        items={menuItems}
        className="sidebar-menu"
      />
      <div className="sidebar-footer">
        <p>笔韵智枢 v0.1.0</p>
      </div>
    </div>
  )
}

export default MainSidebar