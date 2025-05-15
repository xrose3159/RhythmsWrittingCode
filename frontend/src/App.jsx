import React from 'react'
import { Routes, Route } from 'react-router-dom'
import { Layout } from 'antd'
import MainHeader from './components/MainHeader'
import MainSidebar from './components/MainSidebar'
import HomePage from './pages/HomePage'
import FontCreationPage from './pages/FontCreationPage'
import FontPreviewPage from './pages/FontPreviewPage'
import StyleTransferPage from './pages/StyleTransferPage'
import './styles/App.css'

const { Header, Sider, Content } = Layout

function App() {
  return (
    <Layout className="app-container">
      <Header className="app-header">
        <MainHeader />
      </Header>
      <Layout>
        <Sider width={200} className="app-sidebar">
          <MainSidebar />
        </Sider>
        <Content className="app-content">
          <Routes>
            <Route path="/" element={<HomePage />} />
            <Route path="/create" element={<FontCreationPage />} />
            <Route path="/preview" element={<FontPreviewPage />} />
            <Route path="/transfer" element={<StyleTransferPage />} />
          </Routes>
        </Content>
      </Layout>
    </Layout>
  )
}

export default App