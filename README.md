# 🟩 Bale Member Count API

Want to know **how many members** a public **Bale** channel or group has?  
Just use this API &mdash; super easy, super fast!

---

## 🚀 Features

- **Instantly** see member counts of any Bale public channel or group
- Only the **public handle** is needed!
- **JSON** result; easy to use for bots, dashboards, scripts
- Deployed on **Cloudflare Workers** for blazing speed

---

## 🛠️ How to Use

1. **Find the public handle:**  
   Example: `tehranstudio` or any other Bale public channel/group.

2. **Base API endpoint:**  
   ```
   https://bale-member-api.zonercm.workers.dev/{handle}
   ```
   Replace `{handle}` with the group/channel's public handle.

3. **Example:**  
   Checking the member count for the handle `tehranstudio`:
   ```
   https://bale-member-api.zonercm.workers.dev/tehranstudio
   ```

---

## 📦 API Response

You’ll get clean JSON back:

```json
{
  "handle": "tehranstudio",
  "member_count": 12345,
  "type": "channel" // or "group"
}
```
- `handle` — The group/channel handle you provided
- `member_count` — Number of members in that group/channel
- `type` — `"channel"` or `"group"`

---

## 🕹️ Quick Start

### With Your Browser 🌐

Just visit  
```
https://bale-member-api.zonercm.workers.dev/tehranstudio
```
and see the result.

---

### With Curl 🏄

```bash
curl https://bale-member-api.zonercm.workers.dev/tehranstudio
```

---

### In Node.js / JavaScript 👾

```js
async function getMemberCount(handle) {
  const resp = await fetch(
    `https://bale-member-api.zonercm.workers.dev/${handle}`
  );
  const data = await resp.json();
  console.log(`@${handle}:`, data.member_count, "members");
}

getMemberCount("tehranstudio");
```

---

## ⚠️ Notes & Limitations

- The **group/channel must be public** — this will NOT work for private Bale chats.
- If the handle is wrong, missing, private, or doesn't exist, you'll see an error like:

  ```json
  {
    "error": "Channel or group not found or is private."
  }
  ```

---

## 💡 Use Cases

- Show up-to-date Bale group stats on your website
- Track member growth for marketing, analytics, or fun
- Build bots that respond to changes in group size ✨

---

## 📣 Contributing & Feedback

Have ideas, feedback, bug reports, or want to contribute?  
Feel free to [open an issue](#) or even a pull request!

---

## 📜 License

This API is available for public/non-commercial usage.  
Please respect Bale's terms of service and community guidelines.

---

**Made with ❤️ for the Bale community!**
