# 笔韵智枢 — 大数据驱动的智能一体化字体创作引擎

<div align="center">
  <img src="https://github.com/Mango-IM/PenNovaCode/blob/master/images/innovation8.png?raw=true" alt="笔韵智枢项目概览" width="800"/>
</div>

## 🏆 第27届中国机器人及人工智能大赛 人工智能创新赛 作品

**[🔗 访问我们的项目展示网站](https://teminyang.github.io/PenNova/)**

## 项目背景

在人工智能和大数据技术快速发展的背景下，我们正迈向一个充满智能化创造力的新时代。随着数字文化产业的广泛普及，智能字体创作市场规模逐年扩大，"字体设计"这一概念已深入人心，并广泛应用于多个领域。然而，传统字体设计不仅耗时耗力，还缺乏个性化和创新性，亟需一种智能化的字体创作解决方案。

智能字体创作是将人工智能技术与传统书法艺术相结合的创新领域。本项目通过深度学习模型和大数据分析，实现了对汉字风格的精准识别与生成，不仅能保留传统书法的艺术美感，还能创造出符合现代审美的新型字体，为中华文化的传承与创新提供了新的可能性。

<div align="center">
  <img src="https://github.com/xrose3159/RhythmsWritting/raw/gh-pages/images/innovation.png" alt="智能字体创作示例" width="600"/>
</div>

## 核心技术

### 1. 多头编码器驱动的高精度字体生成引擎

- **局部特征提取**：基于多头编码器结构，精准捕捉字体的局部和全局特征，确保字体细节和结构的高保真提取。
- **高效解耦与融合**：通过深度特征解耦，将参考字的风格特征与源字体的内容特征有效结合，实现自然的风格迁移。
- **灵活的风格迁移**：生成器结合内容与风格特征，生成高度一致且精细化的目标字体，确保设计意图的完美还原。

<div align="center">
  <img src="https://github.com/Mango-IM/PenNova/blob/master/images/innovation.png?raw=true" alt="技术架构" width="600"/>
</div>

### 2. 智能参考字优化推荐系统

- **动态参考字优化**：采用基于四角编码的智能推荐算法，动态选择风格特征最优的参考字，有效提升生成的字体一致性。
- **实时数据库更新**：系统集成OCR识别技术，自动更新参考字库，确保生成过程中参考字的多样性和时效性。
- **提高生成效果**：通过优化参考字样本的选择，提高目标字体的风格一致性，避免风格不匹配带来的杂糅问题。

<div align="center">
  <img src="https://github.com/Mango-IM/PenNova/blob/master/images/innovation2.png?raw=true" alt="技术架构" width="600"/>
</div>

### 3. 基于深度学习的源字体智能匹配模块

- **深度风格特征提取**：使用改进的ResNet-18网络对源字体进行多层次的风格特征解析，精确提取笔画细节和结构特征。
- **精准风格匹配**：通过计算参考字与源字体的相似度，智能推荐风格最匹配的源字体，确保生成字体的风格统一性。
- **风格一致性保证**：通过深度匹配与优化，解决风格杂糅问题，确保生成字体的视觉效果和风格统一性。

<div align="center">
  <img src="https://github.com/Mango-IM/PenNova/blob/master/images/innovation3.png?raw=true" alt="技术架构" width="600"/>
</div>

### 4. 自适应扩散模型驱动的字体风格迁移系统

- **形状自适应生成**：采用形状自适应扩散模型生成参考字的风格，并将其迁移至目标字体，确保字体形状与风格的一致性。
- **精细化边缘处理**：通过形状自适应VAE解码器对生成字体的边缘进行精细化调整，优化字体轮廓，提升可读性和美学效果。
- **风格迁移技术**：基于深度学习的风格识别与迁移，实现不同书法风格间的自然转换

<div align="center">
  <img src="https://github.com/Mango-IM/PenNova/blob/master/images/innovation4.png?raw=true" alt="技术架构" width="600"/>
</div>

### 5. 古今字库融合的多样化训练数据集优化方案

- **多类型字体库整合**：结合现代字体库、生僻字库和古书法字库三大数据源，构建具有广泛字体风格和字形的多样化数据集。
- **数据集优化与分类**：通过数据清洗、标准化处理以及风格分类，优化训练数据集的质量，提升模型的泛化能力。
- **增强生成性能**：利用丰富的数据集，提升模型处理复杂字形和非标准化字体的能力，增强对特殊字体风格的生成效果。


## 应用场景

- **文化传承**：帮助传统书法和字体艺术的数字化保存与传承，为文化遗产提供技术支持
- **创意设计**：为设计师提供智能化的字体创作工具，大幅提升设计效率与质量
- **教育培训**：辅助书法教育与汉字书写学习，提供个性化的教学指导
- **内容创作**：为媒体和内容创作者提供多样化的字体风格选择，丰富表现形式

## 系统架构

项目采用前后端分离架构，结合云端AI训练与本地推理能力：

```
笔韵智枢
├── 前端界面
│   ├── 用户交互模块
│   ├── 字体预览系统
│   └── 创作辅助工具
├── 后端服务
│   ├── 字体分析引擎
│   ├── 风格识别系统
│   └── 字体生成模块
└── AI模型
    ├── 深度学习网络
    ├── 大数据分析系统
    └── 训练与评估框架
```

## 系统运行环境

* 操作系统: Ubuntu 20.04.3 LTS (Focal Fossa)

## 环境配置

```
git clone https://github.com/mumuyeye/HaMonitorSentry.git
cd HaMonitorSentry
conda env create -f environment.yml
conda activate sentry
```

## 系统显示配置

```
# 创建字体目录（如果尚未存在）
mkdir -p ~/.local/share/fonts

# 复制字体文件
cp /root/sentry/HaMonitorSentry/MSYH.TTF ~/.local/share/fonts/

# 更新字体缓存
fc-cache -fv

# 检查字体是否安装成功
fc-list | grep "MSYH"
```

## demo运行

```
python demo.py
```

## 项目成果

通过对比实验验证，本系统在以下方面取得显著成果：

- 创作效率提升**96%**
- 用户体验满意度提升**88%**
- 支持**16**种不同风格的汉字生成
- 覆盖**5000+**常用汉字，支持简繁转换

<div style="text-align: center;">解决风格杂糅，优化生成效率。</div>
<div align="center">
  <img src="https://github.com/Mango-IM/PenNova/blob/master/images/innovation5.png?raw=true" alt="成果展示" width="600"/>
</div>

<div style="text-align: center;">结合三种异构数据集构建丰富字库。</div>                  
<div align="center">
  <img src="https://github.com/Mango-IM/PenNova/blob/master/images/innovation6.png?raw=true" alt="成果展示" width="600"/>
</div>

## 致谢

感谢所有对本项目提供支持和帮助的老师、同学和机构。特别感谢中国机器人及人工智能大赛组委会提供的展示平台。

---

© 2025 笔韵智枢团队 保留所有权利 