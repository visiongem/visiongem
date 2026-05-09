## Yane.zZ

Android 工程师。多年时间花在 Kotlin、Jetpack Compose 与系统层 API 上。

**当前空档期**：把过往 Android 生产经验整理成开源资产；开放远程 / 顾问 / 外包等协作机会。

最近主要做：把"官方文档分散、StackOverflow 答案过时、生产事故频发"的领域，简化成**加 3 行依赖、写 3 行代码**。

---

### 代表作品

#### 🔐 [android-secure-toolkit](https://github.com/visiongem/android-secure-toolkit)

3 个独立可发布的 Android 安全库：AES-GCM Keystore 加密 / 强生物识别绑定密钥 / Compose 防截屏。

- **Kotlin 2.0.21** · Jetpack Compose · KSP · JVM 17 · Gradle KTS + Version Catalog
- 零反射、零 DI 框架依赖、3 模块互不依赖
- 10 个 instrumented test 在真 AndroidKeyStore 上端到端通过
- OnePlus 9 / OxygenOS / Android 14 真机验证三模块全部生效
- 想了解设计取舍？读 [PORTFOLIO.md](https://github.com/visiongem/android-secure-toolkit/blob/main/docs/PORTFOLIO.md)（招聘方/客户精读版）
- 想了解未来规划？读 [FUTURE_REPOS.md](https://github.com/visiongem/android-secure-toolkit/blob/main/docs/FUTURE_REPOS.md)（下一个仓库的 idea backlog）

---

### 关注的技术领域

- **Android 平台层精细控制** — Keystore / BiometricPrompt / FLAG_SECURE / WindowManager 等系统 API 的非默认用法
- **密码学工程** — 让 AES-GCM / KDF / IV 不被误用，是工程素养而非数学难题
- **跨传输介质的统一抽象** — BLE / USB / 串口 / 二维码 的"小通道传大消息"问题（计划开第二个仓库）
- **API 设计的反直觉权衡** — 默认安静失败 / 配置不可调弱 / 不绑架 DI 框架

---

### 工作风格速览

```
公开 API:         默认 null 失败 + OrThrow 双形式
关键配置:         硬编码强参数，让弱配置编译期不可能
DI 选择:          中立，不引入 Hilt/Koin/Dagger
文档优先级:       README ≥ docs/*.md ≥ KDoc ≥ 代码注释
AI 协作:          明示边界；设计取舍/真机验证/责任承担由人决定
```

---

### 联系

- **协作 / 合作** → GitHub Issues / Discussions
- **公众号 妮K妮K妮**（同步发 Android、Kotlin、Compose、区块链相关内容）：

  <img src="assets/wechat-qrcode.jpg" alt="妮K妮K妮 公众号二维码" width="200">

- **安全漏洞披露** → 走对应仓库的 [SECURITY.md](https://github.com/visiongem/android-secure-toolkit/blob/main/SECURITY.md)
