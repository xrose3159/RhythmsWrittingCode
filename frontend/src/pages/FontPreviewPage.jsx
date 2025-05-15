import React, { useState } from 'react'
import { Row, Col, Card, Input, Select, Button, Typography, Tabs, List, Tag, Pagination } from 'antd'
import { SearchOutlined, FilterOutlined, DownloadOutlined, StarOutlined, StarFilled } from '@ant-design/icons'
import '../styles/pages/FontPreviewPage.css'

const { Title, Paragraph, Text } = Typography
const { TabPane } = Tabs
const { Option } = Select

const FontPreviewPage = () => {
  const [searchText, setSearchText] = useState('')
  const [selectedStyle, setSelectedStyle] = useState('all')
  const [favorites, setFavorites] = useState([])

  // 字体风格选项
  const fontStyles = [
    { value: 'all', label: '全部' },
    { value: 'kaishu', label: '楷书' },
    { value: 'xingshu', label: '行书' },
    { value: 'caoshu', label: '草书' },
    { value: 'lishu', label: '隶书' },
    { value: 'zhuanshu', label: '篆书' },
    { value: 'songti', label: '宋体' },
    { value: 'heiti', label: '黑体' },
    { value: 'yuanti', label: '圆体' },
    { value: 'fangsong', label: '仿宋' },
    { value: 'modern', label: '现代创意' },
    { value: 'artistic', label: '艺术风格' },
    { value: 'calligraphy', label: '书法风格' },
    { value: 'cartoon', label: '卡通风格' },
    { value: 'handwriting', label: '手写风格' },
    { value: 'elegant', label: '优雅风格' },
    { value: 'bold', label: '粗体风格' },
  ]

  // 模拟字体数据
  const fontData = [
    {
      id: 1,
      name: '清雅楷体',
      style: 'kaishu',
      creator: '笔韵智枢',
      createTime: '2023-05-15',
      downloads: 1256,
      previewImage: '/src/assets/font-preview-1.png',
      tags: ['楷书', '清雅', '正式'],
    },
    {
      id: 2,
      name: '流云行书',
      style: 'xingshu',
      creator: '笔韵智枢',
      createTime: '2023-05-10',
      downloads: 986,
      previewImage: '/src/assets/font-preview-2.png',
      tags: ['行书', '流畅', '艺术'],
    },
    {
      id: 3,
      name: '狂草体',
      style: 'caoshu',
      creator: '笔韵智枢',
      createTime: '2023-05-05',
      downloads: 756,
      previewImage: '/src/assets/font-preview-3.png',
      tags: ['草书', '狂放', '艺术'],
    },
    {
      id: 4,
      name: '古韵篆体',
      style: 'zhuanshu',
      creator: '笔韵智枢',
      createTime: '2023-04-28',
      downloads: 542,
      previewImage: '/src/assets/font-preview-4.png',
      tags: ['篆书', '古韵', '传统'],
    },
    {
      id: 5,
      name: '现代黑体',
      style: 'heiti',
      creator: '笔韵智枢',
      createTime: '2023-04-20',
      downloads: 1568,
      previewImage: '/src/assets/font-preview-5.png',
      tags: ['黑体', '现代', '简洁'],
    },
    {
      id: 6,
      name: '艺术创意体',
      style: 'artistic',
      creator: '笔韵智枢',
      createTime: '2023-04-15',
      downloads: 876,
      previewImage: '/src/assets/font-preview-6.png',
      tags: ['创意', '艺术', '现代'],
    },
  ]

  // 处理收藏切换
  const toggleFavorite = (fontId) => {
    if (favorites.includes(fontId)) {
      setFavorites(favorites.filter(id => id !== fontId))
    } else {
      setFavorites([...favorites, fontId])
    }
  }

  // 过滤字体数据
  const filteredFonts = fontData.filter(font => {
    const matchesSearch = searchText === '' || 
      font.name.toLowerCase().includes(searchText.toLowerCase()) ||
      font.tags.some(tag => tag.toLowerCase().includes(searchText.toLowerCase()))
    
    const matchesStyle = selectedStyle === 'all' || font.style === selectedStyle
    
    return matchesSearch && matchesStyle
  })

  return (
    <div className="font-preview-page">
      <Title level={2}>字体预览</Title>
      <Paragraph className="page-description">
        浏览和预览系统中的所有字体，支持按风格筛选和搜索。
      </Paragraph>
      
      <Card className="filter-card">
        <Row gutter={[16, 16]} align="middle">
          <Col xs={24} sm={12} md={8} lg={6}>
            <Input
              placeholder="搜索字体名称或标签"
              prefix={<SearchOutlined />}
              value={searchText}
              onChange={e => setSearchText(e.target.value)}
            />
          </Col>
          <Col xs={24} sm={12} md={8} lg={6}>
            <Select
              placeholder="选择字体风格"
              style={{ width: '100%' }}
              value={selectedStyle}
              onChange={value => setSelectedStyle(value)}
            >
              {fontStyles.map(style => (
                <Option key={style.value} value={style.value}>{style.label}</Option>
              ))}
            </Select>
          </Col>
          <Col xs={24} sm={24} md={8} lg={12} className="filter-actions">
            <Button icon={<FilterOutlined />}>更多筛选</Button>
          </Col>
        </Row>
      </Card>
      
      <Tabs defaultActiveKey="all" className="preview-tabs">
        <TabPane tab="全部字体" key="all">
          <div className="fonts-grid">
            <List
              grid={{ gutter: 24, xs: 1, sm: 2, md: 3, lg: 3, xl: 4, xxl: 4 }}
              dataSource={filteredFonts}
              renderItem={font => (
                <List.Item>
                  <Card
                    className="font-card"
                    cover={
                      <div className="font-preview">
                        <div className="preview-text">和而不同</div>
                        <div className="preview-text">美美与共</div>
                      </div>
                    }
                    actions={[
                      <Button type="text" icon={<DownloadOutlined />}>下载</Button>,
                      favorites.includes(font.id) ? 
                        <Button type="text" icon={<StarFilled />} onClick={() => toggleFavorite(font.id)}>已收藏</Button> :
                        <Button type="text" icon={<StarOutlined />} onClick={() => toggleFavorite(font.id)}>收藏</Button>
                    ]}
                  >
                    <Card.Meta
                      title={font.name}
                      description={
                        <div>
                          <div className="font-info">
                            <Text type="secondary">创建者: {font.creator}</Text>
                            <Text type="secondary">下载: {font.downloads}</Text>
                          </div>
                          <div className="font-tags">
                            {font.tags.map((tag, index) => (
                              <Tag key={index}>{tag}</Tag>
                            ))}
                          </div>
                        </div>
                      }
                    />
                  </Card>
                </List.Item>
              )}
            />
          </div>
          <div className="pagination-container">
            <Pagination defaultCurrent={1} total={50} />
          </div>
        </TabPane>
        <TabPane tab="我的收藏" key="favorites">
          <div className="fonts-grid">
            <List
              grid={{ gutter: 24, xs: 1, sm: 2, md: 3, lg: 3, xl: 4, xxl: 4 }}
              dataSource={filteredFonts.filter(font => favorites.includes(font.id))}
              renderItem={font => (
                <List.Item>
                  <Card
                    className="font-card"
                    cover={
                      <div className="font-preview">
                        <div className="preview-text">和而不同</div>
                        <div className="preview-text">美美与共</div>
                      </div>
                    }
                    actions={[
                      <Button type="text" icon={<DownloadOutlined />}>下载</Button>,
                      <Button type="text" icon={<StarFilled />} onClick={() => toggleFavorite(font.id)}>取消收藏</Button>
                    ]}
                  >
                    <Card.Meta
                      title={font.name}
                      description={
                        <div>
                          <div className="font-info">
                            <Text type="secondary">创建者: {font.creator}</Text>
                            <Text type="secondary">下载: {font.downloads}</Text>
                          </div>
                          <div className="font-tags">
                            {font.tags.map((tag, index) => (
                              <Tag key={index}>{tag}</Tag>
                            ))}
                          </div>
                        </div>
                      }
                    />
                  </Card>
                </List.Item>
              )}
              locale={{ emptyText: '暂无收藏字体' }}
            />
          </div>
        </TabPane>
        <TabPane tab="最近使用" key="recent">
          <div className="empty-message">
            <Paragraph>暂无最近使用记录</Paragraph>
          </div>
        </TabPane>
      </Tabs>
    </div>
  )
}

export default FontPreviewPage