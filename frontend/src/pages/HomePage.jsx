import React from 'react'
import { Row, Col, Card, Button, Typography, Carousel, Statistic } from 'antd'
import { EditOutlined, EyeOutlined, SwapOutlined, BookOutlined } from '@ant-design/icons'
import '../styles/pages/HomePage.css'

const { Title, Paragraph } = Typography

const HomePage = () => {
  // 轮播图数据
  const carouselItems = [
    {
      title: '智能字体创作',
      description: '结合AI技术与传统书法艺术，实现智能化的汉字字体创作',
      image: '/src/assets/carousel-1.jpg',
    },
    {
      title: '多风格字体生成',
      description: '支持16种不同风格的汉字生成，覆盖5000+常用汉字',
      image: '/src/assets/carousel-2.jpg',
    },
    {
      title: '风格迁移技术',
      description: '基于深度学习的风格识别与迁移，实现不同书法风格间的自然转换',
      image: '/src/assets/carousel-3.jpg',
    },
  ]

  // 功能特点数据
  const features = [
    {
      icon: <EditOutlined />,
      title: '智能创作',
      description: '结合用户交互和AI算法，自动识别和推荐最适合的参考字样式',
    },
    {
      icon: <EyeOutlined />,
      title: '高清预览',
      description: '支持超高清字体渲染，保证笔画细节和艺术表现力',
    },
    {
      icon: <SwapOutlined />,
      title: '风格迁移',
      description: '实现不同书法风格间的自然转换，创造个性化字体',
    },
    {
      icon: <BookOutlined />,
      title: '文化传承',
      description: '帮助传统书法和字体艺术的数字化保存与传承',
    },
  ]

  return (
    <div className="home-page">
      {/* 轮播图部分 */}
      <Carousel autoplay className="home-carousel">
        {carouselItems.map((item, index) => (
          <div key={index} className="carousel-item">
            <div className="carousel-content">
              <Title level={2}>{item.title}</Title>
              <Paragraph>{item.description}</Paragraph>
              <Button type="primary" size="large">
                立即体验
              </Button>
            </div>
          </div>
        ))}
      </Carousel>

      {/* 统计数据部分 */}
      <div className="statistics-section">
        <Row gutter={[32, 32]} justify="center">
          <Col span={6}>
            <Statistic title="创作效率提升" value={96} suffix="%" />
          </Col>
          <Col span={6}>
            <Statistic title="用户满意度" value={88} suffix="%" />
          </Col>
          <Col span={6}>
            <Statistic title="支持字体风格" value={16} suffix="种" />
          </Col>
          <Col span={6}>
            <Statistic title="覆盖汉字" value="5000+" />
          </Col>
        </Row>
      </div>

      {/* 功能特点部分 */}
      <div className="features-section">
        <Title level={2} className="section-title">功能特点</Title>
        <Row gutter={[32, 32]}>
          {features.map((feature, index) => (
            <Col xs={24} sm={12} md={6} key={index}>
              <Card className="feature-card">
                <div className="feature-icon">{feature.icon}</div>
                <Title level={4}>{feature.title}</Title>
                <Paragraph>{feature.description}</Paragraph>
              </Card>
            </Col>
          ))}
        </Row>
      </div>

      {/* 应用场景部分 */}
      <div className="scenarios-section">
        <Title level={2} className="section-title">应用场景</Title>
        <Row gutter={[32, 32]}>
          <Col span={12}>
            <Card title="文化传承" className="scenario-card">
              <Paragraph>
                帮助传统书法和字体艺术的数字化保存与传承，为文化遗产提供技术支持。
              </Paragraph>
            </Card>
          </Col>
          <Col span={12}>
            <Card title="创意设计" className="scenario-card">
              <Paragraph>
                为设计师提供智能化的字体创作工具，大幅提升设计效率与质量。
              </Paragraph>
            </Card>
          </Col>
          <Col span={12}>
            <Card title="教育培训" className="scenario-card">
              <Paragraph>
                辅助书法教育与汉字书写学习，提供个性化的教学指导。
              </Paragraph>
            </Card>
          </Col>
          <Col span={12}>
            <Card title="内容创作" className="scenario-card">
              <Paragraph>
                为媒体和内容创作者提供多样化的字体风格选择，丰富表现形式。
              </Paragraph>
            </Card>
          </Col>
        </Row>
      </div>

      {/* 开始使用部分 */}
      <div className="get-started-section">
        <Title level={2}>开始使用笔韵智枢</Title>
        <Paragraph>
          立即体验AI驱动的智能字体创作系统，释放您的创意潜能
        </Paragraph>
        <Button type="primary" size="large">
          开始创作
        </Button>
      </div>
    </div>
  )
}

export default HomePage