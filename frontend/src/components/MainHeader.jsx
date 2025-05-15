import React from 'react'
import { Layout, Menu, Button, Avatar, Dropdown } from 'antd'
import { UserOutlined, BellOutlined, SettingOutlined } from '@ant-design/icons'
import { Link } from 'react-router-dom'
import '../styles/components/MainHeader.css'

const MainHeader = () => {
  const userMenuItems = [
    {
      key: 'profile',
      label: '个人中心',
    },
    {
      key: 'settings',
      label: '设置',
    },
    {
      key: 'logout',
      label: '退出登录',
    },
  ]

  return (
    <div className="main-header">
      <div className="logo">
        <Link to="/">
          <h1>笔韵智枢</h1>
        </Link>
      </div>
      <div className="header-menu">
        <Menu mode="horizontal" defaultSelectedKeys={['home']}>
          <Menu.Item key="home">
            <Link to="/">首页</Link>
          </Menu.Item>
          <Menu.Item key="create">
            <Link to="/create">字体创作</Link>
          </Menu.Item>
          <Menu.Item key="preview">
            <Link to="/preview">字体预览</Link>
          </Menu.Item>
          <Menu.Item key="transfer">
            <Link to="/transfer">风格迁移</Link>
          </Menu.Item>
        </Menu>
      </div>
      <div className="header-actions">
        <Button type="primary" className="create-btn">
          开始创作
        </Button>
        <BellOutlined className="notification-icon" />
        <Dropdown menu={{ items: userMenuItems }} placement="bottomRight">
          <Avatar icon={<UserOutlined />} />
        </Dropdown>
      </div>
    </div>
  )
}

export default MainHeader