import React, { useState } from 'react'
import { Row, Col, Card, Form, Input, Select, Button, Upload, Tabs, Divider, Typography, message } from 'antd'
import { UploadOutlined, FontSizeOutlined, BgColorsOutlined, HighlightOutlined } from '@ant-design/icons'
import '../styles/pages/FontCreationPage.css'

const { Title, Paragraph } = Typography
const { TabPane } = Tabs
const { Option } = Select

const FontCreationPage = () => {
  const [form] = Form.useForm()
  const [currentStep, setCurrentStep] = useState(1)
  const [referenceFont, setReferenceFont] = useState(null)
  const [generatedPreview, setGeneratedPreview] = useState(null)
  
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

  // 处理表单提交
  const handleSubmit = (values) => {
    console.log('表单值:', values)
    message.success('字体生成请求已提交，正在处理...')
    
    // 模拟生成结果
    setTimeout(() => {
      setGeneratedPreview('/src/assets/generated-font-preview.png')
      setCurrentStep(3)
      message.success('字体生成完成！')
    }, 2000)
  }

  // 上传参考字样式
  const handleReferenceUpload = (info) => {
    if (info.file.status === 'done') {
      setReferenceFont(info.file.response.url)
      message.success(`${info.file.name} 上传成功`)
      setCurrentStep(2)
    } else if (info.file.status === 'error') {
      message.error(`${info.file.name} 上传失败`)
    }
  }

  // 重新开始创作
  const handleReset = () => {
    form.resetFields()
    setReferenceFont(null)
    setGeneratedPreview(null)
    setCurrentStep(1)
  }

  return (
    <div className="font-creation-page">
      <Title level={2}>智能字体创作</Title>
      <Paragraph className="page-description">
        通过AI技术，将您的参考字样式转化为完整的字体，支持多种风格和个性化定制。
      </Paragraph>
      
      <Tabs activeKey={`step${currentStep}`} className="creation-tabs">
        <TabPane tab="步骤1: 选择参考字" key="step1">
          <Card className="step-card">
            <Row gutter={[24, 24]}>
              <Col span={12}>
                <div className="upload-section">
                  <Title level={4}>上传参考字样式</Title>
                  <Paragraph>
                    上传您喜欢的字体样式图片，系统将分析并提取其特征。
                    建议上传清晰的黑色字体图片，背景为白色。
                  </Paragraph>
                  <Upload
                    name="referenceFont"
                    listType="picture-card"
                    className="reference-uploader"
                    showUploadList={false}
                    action="https://www.mocky.io/v2/5cc8019d300000980a055e76"
                    onChange={handleReferenceUpload}
                  >
                    {referenceFont ? (
                      <img src={referenceFont} alt="参考字" style={{ width: '100%' }} />
                    ) : (
                      <div>
                        <UploadOutlined />
                        <div style={{ marginTop: 8 }}>上传参考字</div>
                      </div>
                    )}
                  </Upload>
                </div>
              </Col>
              <Col span={12}>
                <div className="reference-guide">
                  <Title level={4}>参考字指南</Title>
                  <Paragraph>
                    <ul>
                      <li>选择有代表性的汉字，如"永"、"德"等</li>
                      <li>确保图片清晰，笔画完整</li>
                      <li>避免使用有复杂背景的图片</li>
                      <li>可以上传手写字体或印刷字体</li>
                    </ul>
                  </Paragraph>
                  <div className="sample-references">
                    <Title level={5}>推荐参考字示例：</Title>
                    <div className="sample-images">
                      {/* 这里放示例图片 */}
                      <div className="sample-image">永</div>
                      <div className="sample-image">德</div>
                      <div className="sample-image">和</div>
                      <div className="sample-image">美</div>
                    </div>
                  </div>
                </div>
              </Col>
            </Row>
            <div className="step-actions">
              <Button type="primary" onClick={() => setCurrentStep(2)} disabled={!referenceFont}>
                下一步
              </Button>
            </div>
          </Card>
        </TabPane>
        
        <TabPane tab="步骤2: 设置字体参数" key="step2">
          <Card className="step-card">
            <Form
              form={form}
              layout="vertical"
              onFinish={handleSubmit}
              initialValues={{
                style: 'kaishu',
                thickness: 'medium',
                contrast: 'medium',
                creativity: 'medium',
              }}
            >
              <Row gutter={[24, 24]}>
                <Col span={12}>
                  <Form.Item
                    name="style"
                    label="字体风格"
                    rules={[{ required: true, message: '请选择字体风格' }]}
                  >
                    <Select placeholder="选择字体风格">
                      {fontStyles.map(style => (
                        <Option key={style.value} value={style.value}>{style.label}</Option>
                      ))}
                    </Select>
                  </Form.Item>
                  
                  <Form.Item
                    name="thickness"
                    label="笔画粗细"
                    rules={[{ required: true, message: '请选择笔画粗细' }]}
                  >
                    <Select placeholder="选择笔画粗细">
                      <Option value="thin">细</Option>
                      <Option value="medium">中等</Option>
                      <Option value="thick">粗</Option>
                    </Select>
                  </Form.Item>
                  
                  <Form.Item
                    name="contrast"
                    label="对比度"
                    rules={[{ required: true, message: '请选择对比度' }]}
                  >
                    <Select placeholder="选择对比度">
                      <Option value="low">低</Option>
                      <Option value="medium">中等</Option>
                      <Option value="high">高</Option>
                    </Select>
                  </Form.Item>
                </Col>
                
                <Col span={12}>
                  <Form.Item
                    name="creativity"
                    label="创意程度"
                    rules={[{ required: true, message: '请选择创意程度' }]}
                  >
                    <Select placeholder="选择创意程度">
                      <Option value="low">保守</Option>
                      <Option value="medium">平衡</Option>
                      <Option value="high">创新</Option>
                    </Select>
                  </Form.Item>
                  
                  <Form.Item
                    name="sampleText"
                    label="预览文本"
                  >
                    <Input.TextArea
                      placeholder="输入要预览的文本"
                      rows={4}
                      defaultValue="和而不同 美美与共"
                    />
                  </Form.Item>
                </Col>
              </Row>
              
              <Divider />
              
              <div className="reference-preview">
                <Title level={4}>参考字预览</Title>
                <div className="preview-image">
                  {referenceFont && <img src={referenceFont} alt="参考字预览" />}
                </div>
              </div>
              
              <div className="step-actions">
                <Button onClick={() => setCurrentStep(1)} style={{ marginRight: 16 }}>
                  上一步
                </Button>
                <Button type="primary" htmlType="submit">
                  生成字体
                </Button>
              </div>
            </Form>
          </Card>
        </TabPane>
        
        <TabPane tab="步骤3: 字体生成结果" key="step3">
          <Card className="step-card">
            <div className="result-section">
              <Title level={4}>生成结果</Title>
              
              <div className="generated-preview">
                {generatedPreview ? (
                  <div className="preview-container">
                    <div className="preview-image">
                      <img src={generatedPreview} alt="生成的字体预览" />
                    </div>
                    <div className="preview-text">
                      <div className="text-sample">和而不同 美美与共</div>
                      <div className="text-sample">天行健 君子以自强不息</div>
                      <div className="text-sample">厚德载物 自强不息</div>
                    </div>
                  </div>
                ) : (
                  <div className="generating-message">
                    正在生成字体，请稍候...
                  </div>
                )}
              </div>
              
              <div className="result-actions">
                <Button type="primary" style={{ marginRight: 16 }}>
                  下载字体文件
                </Button>
                <Button type="primary" style={{ marginRight: 16 }}>
                  保存到我的字体
                </Button>
                <Button onClick={handleReset}>
                  重新创作
                </Button>
              </div>
            </div>
          </Card>
        </TabPane>
      </Tabs>
    </div>
  )
}

export default FontCreationPage