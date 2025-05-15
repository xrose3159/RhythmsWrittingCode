import React, { useState } from 'react'
import { Row, Col, Card, Form, Input, Select, Button, Upload, Typography, Divider, message, Slider } from 'antd'
import { UploadOutlined, SwapOutlined, SaveOutlined, UndoOutlined } from '@ant-design/icons'
import '../styles/pages/StyleTransferPage.css'

const { Title, Paragraph } = Typography
const { Option } = Select

const StyleTransferPage = () => {
  const [form] = Form.useForm()
  const [sourceImage, setSourceImage] = useState(null)
  const [targetStyle, setTargetStyle] = useState(null)
  const [resultImage, setResultImage] = useState(null)
  const [transferStrength, setTransferStrength] = useState(50)
  
  // 字体风格选项
  const fontStyles = [
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

  // 处理源图片上传
  const handleSourceUpload = (info) => {
    if (info.file.status === 'done') {
      setSourceImage(info.file.response.url)
      message.success(`${info.file.name} 上传成功`)
    } else if (info.file.status === 'error') {
      message.error(`${info.file.name} 上传失败`)
    }
  }

  // 处理目标风格上传
  const handleTargetStyleUpload = (info) => {
    if (info.file.status === 'done') {
      setTargetStyle(info.file.response.url)
      message.success(`${info.file.name} 上传成功`)
    } else if (info.file.status === 'error') {
      message.error(`${info.file.name} 上传失败`)
    }
  }

  // 处理风格迁移
  const handleStyleTransfer = () => {
    if (!sourceImage) {
      message.error('请先上传源字体图片')
      return
    }
    
    if (!targetStyle && !form.getFieldValue('stylePreset')) {
      message.error('请上传目标风格图片或选择预设风格')
      return
    }
    
    message.loading('正在进行风格迁移，请稍候...', 2)
    
    // 模拟风格迁移结果
    setTimeout(() => {
      setResultImage('/src/assets/style-transfer-result.png')
      message.success('风格迁移完成！')
    }, 2000)
  }

  // 重置所有内容
  const handleReset = () => {
    form.resetFields()
    setSourceImage(null)
    setTargetStyle(null)
    setResultImage(null)
    setTransferStrength(50)
  }

  // 保存结果
  const handleSaveResult = () => {
    if (resultImage) {
      message.success('结果已保存到我的字体')
    }
  }

  return (
    <div className="style-transfer-page">
      <Title level={2}>风格迁移</Title>
      <Paragraph className="page-description">
        将一种字体风格应用到另一种字体上，创造独特的混合风格字体。
      </Paragraph>
      
      <Row gutter={[24, 24]}>
        <Col span={24} md={16}>
          <Card className="main-card">
            <Form form={form} layout="vertical">
              <Row gutter={[24, 24]}>
                <Col span={12}>
                  <Form.Item label="源字体图片" required>
                    <Upload
                      name="sourceImage"
                      listType="picture-card"
                      className="upload-container"
                      showUploadList={false}
                      action="https://www.mocky.io/v2/5cc8019d300000980a055e76"
                      onChange={handleSourceUpload}
                    >
                      {sourceImage ? (
                        <img src={sourceImage} alt="源字体" style={{ width: '100%' }} />
                      ) : (
                        <div>
                          <UploadOutlined />
                          <div style={{ marginTop: 8 }}>上传源字体</div>
                        </div>
                      )}
                    </Upload>
                    <Paragraph type="secondary" className="upload-tip">
                      上传您想要改变风格的字体图片
                    </Paragraph>
                  </Form.Item>
                </Col>
                
                <Col span={12}>
                  <Form.Item label="目标风格">
                    <Tabs defaultActiveKey="preset">
                      <TabPane tab="预设风格" key="preset">
                        <Form.Item name="stylePreset" noStyle>
                          <Select placeholder="选择预设风格">
                            {fontStyles.map(style => (
                              <Option key={style.value} value={style.value}>{style.label}</Option>
                            ))}
                          </Select>
                        </Form.Item>
                      </TabPane>
                      <TabPane tab="上传风格" key="upload">
                        <Upload
                          name="targetStyle"
                          listType="picture-card"
                          className="upload-container"
                          showUploadList={false}
                          action="https://www.mocky.io/v2/5cc8019d300000980a055e76"
                          onChange={handleTargetStyleUpload}
                        >
                          {targetStyle ? (
                            <img src={targetStyle} alt="目标风格" style={{ width: '100%' }} />
                          ) : (
                            <div>
                              <UploadOutlined />
                              <div style={{ marginTop: 8 }}>上传风格</div>
                            </div>
                          )}
                        </Upload>
                      </TabPane>
                    </Tabs>
                    <Paragraph type="secondary" className="upload-tip">
                      选择预设风格或上传您喜欢的风格图片
                    </Paragraph>
                  </Form.Item>
                </Col>
              </Row>
              
              <Divider />
              
              <Form.Item label="迁移强度">
                <Slider
                  min={0}
                  max={100}
                  value={transferStrength}
                  onChange={setTransferStrength}
                  tooltipVisible
                  tooltipPlacement="bottom"
                  tipFormatter={value => `${value}%`}
                />
                <Row justify="space-between">
                  <Col>保留原字体特征</Col>
                  <Col>完全采用新风格</Col>
                </Row>
              </Form.Item>
              
              <Form.Item label="预览文本">
                <Input.TextArea
                  placeholder="输入要预览的文本"
                  rows={2}
                  defaultValue="和而不同 美美与共"
                />
              </Form.Item>
              
              <Form.Item>
                <Button
                  type="primary"
                  icon={<SwapOutlined />}
                  onClick={handleStyleTransfer}
                  className="transfer-btn"
                >
                  开始风格迁移
                </Button>
                <Button
                  icon={<UndoOutlined />}
                  onClick={handleReset}
                  style={{ marginLeft: 16 }}
                >
                  重置
                </Button>
              </Form.Item>
            </Form>
          </Card>
        </Col>
        
        <Col span={24} md={8}>
          <Card className="result-card" title="迁移结果">
            {resultImage ? (
              <div className="result-container">
                <div className="result-image">
                  <img src={resultImage} alt="迁移结果" />
                </div>
                <div className="result-text">
                  <div className="text-sample">和而不同</div>
                  <div className="text-sample">美美与共</div>
                  <div className="text-sample">天行健</div>
                </div>
                <div className="result-actions">
                  <Button
                    type="primary"
                    icon={<SaveOutlined />}
                    onClick={handleSaveResult}
                  >
                    保存结果
                  </Button>
                  <Button type="link">下载图片</Button>
                </div>
              </div>
            ) : (
              <div className="empty-result">
                <Paragraph className="empty-text">
                  完成设置后点击「开始风格迁移」按钮生成结果
                </Paragraph>
              </div>
            )}
          </Card>
          
          <Card className="tips-card" title="使用提示" style={{ marginTop: 24 }}>
            <ul className="tips-list">
              <li>选择清晰的源字体图片，确保笔画完整</li>
              <li>调整迁移强度可以控制风格融合的程度</li>
              <li>可以尝试不同的预设风格，找到最适合的效果</li>
              <li>上传自定义风格图片可以创造更个性化的字体</li>
              <li>生成的结果可以保存到我的字体库中重复使用</li>
            </ul>
          </Card>
        </Col>
      </Row>
    </div>
  )
}

export default StyleTransferPage

const { TabPane } = Tabs
const Tabs = Tabs || { TabPane: ({children}) => children }