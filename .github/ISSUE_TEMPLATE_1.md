name: Issues Release Rule
description: 通过这个模板发布你的问题
body:
  - type: markdown
    attributes:
      value: |
        请遵循模板发布问题
  - type: textarea
    id: text
    attributes:
      label: 你的问题/建议/想说的内容是什么?
      description: 提出问题前，先看看主页中的 "下载前你需要知晓的内容:" <br/> 发布问题前请检查是否有重复的 <br/> 如果是反馈bug，请先确定是由汉化导致的，否则请在原版的Issues提交问题
      placeholder: "说些什么？建议尽可能清晰的描述问题"
    validations:
      required: true
  - type: textarea
    id: version
    attributes:
      label: 版本
      description: 这个问题发生在哪个版本? <br/> 如果是建议，汉化或故障请填写当前最新的版本
      placeholder: "no-version"
    validations:
      required: true
