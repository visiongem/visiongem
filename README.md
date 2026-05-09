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
- 已发版 JitPack v0.1.0：[各模块详细文档](https://github.com/visiongem/android-secure-toolkit/tree/main/docs)

#### 📨 [android-message-pipeline](https://github.com/visiongem/android-message-pipeline)

"小通道传大消息"的统一抽象——BLE GATT (MTU 23) / USB Bulk / 串口 / 二维码 / Socket 等任何受 MTU 限制的通道，都能用同一套分片 + 重组 + 异步分发协议。

- 4 个核心抽象：`Codec` / `Chunker` / `Transport` / `PipelineDispatcher`
- 默认实现含 `[index:total:hash:groupId]` 头格式分片协议（顺序无关 + 多组并发）
- 双线程异步管道（IO 与业务解耦）+ 7 个单元测试覆盖核心逻辑

#### 🧰 [android-kotlin-utils](https://github.com/visiongem/android-kotlin-utils)

自用 Android 扩展函数集——金融场景常用 + Compose 时代痛点两类。

- `numeric`：金额安全转换（拒绝静默截断）+ Hex 编解码
- `string`：敏感字段 mask（手机号 / 邮箱 / 身份证）+ 内存安全 zeroize
- `compose`：防抖点击 Modifier + 条件式 Modifier
- `lifecycle`：生命周期感知 Flow 收集（避免内存泄漏）
- 23 个单元测试全绿

---

### 关注的技术领域

- **Android 平台层精细控制** — Keystore / BiometricPrompt / FLAG_SECURE / WindowManager 等系统 API 的非默认用法
- **密码学工程** — 让 AES-GCM / KDF / IV 不被误用，是工程素养而非数学难题
- **跨传输介质的统一抽象** — BLE / USB / 串口 / 二维码 的"小通道传大消息"问题
- **API 设计的反直觉权衡** — 默认安静失败 / 配置不可调弱 / 不绑架 DI 框架
- **长期项目的技术债清理** — Java→Kotlin / RxJava→Coroutine / ViewBinding→Compose / M2→M3 等大规模平滑迁移

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
