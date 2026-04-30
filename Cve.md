Got it — you want a **universal, copy-paste command set** that works across **most Linux distros (Debian, Ubuntu, Alpine, RHEL, Amazon Linux, etc.)**, especially for containers + hosts.

Below is a **compact “run anywhere” checklist** 👇

---

# 🧪 ✅ Universal Vulnerability Check Commands

## 1️⃣ Kernel version (MOST IMPORTANT)

```bash
uname -r
```

👉 If kernel is **not updated recently (April 2026+) → likely vulnerable**

---

## 2️⃣ Check if vulnerable module is loaded

```bash
(lsmod 2>/dev/null || cat /proc/modules) | grep algif_aead
```

👉 Works across:

* Debian/Ubuntu ✅
* Alpine ✅
* RHEL/Amazon Linux ✅
* Containers (even minimal) ✅

---

## 3️⃣ Check if module exists (even if not loaded)

```bash
(find /lib/modules/$(uname -r) -type f 2>/dev/null || true) | grep algif_aead
```

👉 If found → feature exists → exploitable path possible

---

## 4️⃣ Check AF_ALG socket availability (real exploit path)

```bash
python3 - << 'EOF'
import socket
try:
    socket.socket(socket.AF_ALG, socket.SOCK_SEQPACKET, 0)
    print("AF_ALG available → RISK")
except:
    print("AF_ALG not available")
EOF
```

👉 If this prints **RISK → vulnerable surface confirmed**

---

## 5️⃣ Container risk check (important for you)

```bash
id && (capsh --print 2>/dev/null | grep cap_sys_admin || echo "No extra caps")
```

👉 If:

* `uid=0(root)` OR
* `cap_sys_admin` present

➡️ Exploitation becomes much easier

---

## 🚀 6️⃣ One-liner (quick audit script)

Copy-paste this anywhere:

```bash
echo "Kernel: $(uname -r)" && \
echo "---- Module ----" && \
((lsmod 2>/dev/null || cat /proc/modules) | grep algif_aead || echo "Not loaded") && \
echo "---- AF_ALG ----" && \
python3 - << 'EOF'
import socket
try:
    socket.socket(socket.AF_ALG, socket.SOCK_SEQPACKET, 0)
    print("AF_ALG available → RISK")
except:
    print("AF_ALG not available")
EOF
```

---

# 📊 How to interpret results

| Result              | Meaning          |
| ------------------- | ---------------- |
| Old kernel          | ❌ Vulnerable     |
| `algif_aead` loaded | ⚠️ Higher risk   |
| AF_ALG works        | 🔥 Exploitable   |
| Root container      | 💣 Critical risk |

---

# 🛡️ Universal Fix Command (All Distros)

## Temporary mitigation:

```bash
sudo modprobe -r algif_aead 2>/dev/null
echo "blacklist algif_aead" | sudo tee /etc/modprobe.d/disable-algif.conf
```

---

## Permanent fix (by distro)

### Debian / Ubuntu

```bash
sudo apt update && sudo apt upgrade -y
```

### Alpine

```bash
apk update && apk upgrade
```

### RHEL / Amazon Linux / CentOS

```bash
sudo yum update -y
```

---

# ⚠️ Critical Reminder (Containers)

👉 For **Docker / Kubernetes / EKS**:

* ❗ Container checks are **NOT enough**
* ✅ You MUST check **host kernel**

```bash
uname -r
```

---

# ⚡ Bottom line

If **ANY of these are true**:

* Kernel outdated
* AF_ALG works
* Module exists

👉 Treat system as **VULNERABLE → PATCH IMMEDIATELY**

---

## 👍 If you want next

I can:

* Give you a **Kubernetes DaemonSet script** to scan all nodes
* Or **EKS-specific patch steps (very relevant for you)**
