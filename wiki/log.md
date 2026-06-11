# 操作日志

## [2026-06-11] sync | 重构 HTML PPT 为六部曲架构
- **变更**: 将 `ppt/html-deck/` 从五部分调整为六部分
  - Part 1「政策锚定」精简为 6 页（移除案例内容，保留 P2-P5 + 精简版 P14 过渡）
  - Part 2「技术祛魅」保持 6 页不变
  - Part 3「同行压力」独立为 9 页（移除原 P29-P30）
  - 新增 Part 4「中建智能实践」10 页（P6-P13 + P29-P30 移入，P6 去掉上排国内信号、加过渡文案）
  - Part 5「落地路径」8 页（原 Part 4 顺延）
  - Part 6「风险预判与行动倡议」10 页（原 Part 5 顺延，新增 part6-cover.html 过渡页）
  - 更新 `index.html` DECK_MANIFEST 放映顺序
  - 批量更新 40+ 个 slide 的 part-label 与过渡页标题
  - 更新 `DECK-MANIFEST.md` 页面清单
- **冲突**: 无
