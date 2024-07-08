## 项目名称  
Knowledge Flow知流在线编辑器
## 项目成员  
队长：吴\*霖  
队员：宋\*  
队员：王\*悦  
## 项目目标  
**功能一：智能润色**

1、在功能上：利用大语言模型，根据上下文，实现如摘要、修饰、续写、病句改写、翻译等等常见写作辅助功能；
2、在交互形式上：需要考虑到不同能力的整合、管理与切换，降低用户选择负担。

选手可面对某一或某多个特定场景，如大创项目书文档撰写、竞赛文书撰写、代码编辑等，进行功能的合理策划，不求多而全，要把产品置于特定的场景之下，基于对场景的真实有效洞察，进行功能的精致布局。

**功能二：多媒体信息提取**
1、在功能上：利用OCR、目标检测和语音识别等多模态感知技术，实现对图像（如截图、海报、pdf等）、语音甚至视频等多媒体信息的在线信息提取，并能允许用户将内容有机整合到编辑器中。
2、在交互形式上：能够有效的管理和检索多模态数据。

除了做多模态信息的转录，选手也可以关注多模态数据，如何作为专业领域知识库，成为可以重复利用的结构化知识，丰富编辑器的专业知识辅助能力。

**功能三：智能格式排版**
1、在功能上：根据内容类型识别，自动进行格式排版，如自动调整字体、字号、行间距等，同时提供多种排版模板供用户选择。
2、在交互形式上：注重样式库的管理和二次编辑。

选手可以考虑手动输入样式规则，或提取已有文章的格式，两种方式。

**附加功能：智能信息可视化**
1、在功能上：根据内容及可视化类型，结合大语言模型，进行包括但不限于表格生成、思维导图生成和数据可视化生成等功能。
2、在交互形式上：选手可以自由发挥，加入动态可视化效果、画布二次编辑等符合用户体验需求的创意点。



小模型指定部署/调用平台：OCR、目标检测和语音识别模型等小模型指定平台：飞桨AI Studio星河社区。模型均基于飞桨PaddlePaddle深度学习框架。

大模型指定调用工具：星河社区ERNIE SDK。大模型能力基于文心大模型。

产品服务部署与网站托管指定平台：飞桨AI Studio星河社区，提供网站部署环境。

 
## 项目文件夹说明  
EditEnd：后端相关文件，包括数据库的管理与存储  
EditFont：前端相关文件，包括网页的布局与设计
## 项目技术栈  
1.大模型：文心大模型   
2.数据库：MySQL  
3.网页端框架：Vue3    
4.小模型：飞桨PaddlePaddle深度学习框架  
## To do  
- []1. 昼夜模式切换
- []2. 其他部分样式调整
- []3. 前端用户名验证，用户名不能出现空格
- []4. 模型推理时加载页面
- []5. 生成思维导图
- []6. 一键格式转换
- []7. markdown格式渲染
- []8. 后端部署服务器
- []9. 前端部署




