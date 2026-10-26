const messages = document.getElementById("messages");
const input = document.getElementById("input");
const sendBtn = document.getElementById("send");

function addMessage(text, who) {
  const div = document.createElement("div");
  div.className = "msg " + who;
  div.textContent = text;
  messages.appendChild(div);
  messages.scrollTop = messages.scrollHeight;
}

async function send() {
  const text = input.value.trim();
  if (!text) return;
  addMessage(text, "user");
  input.value = "";
  try {
    const res = await fetch("/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: text })
    });
    const data = await res.json();
    addMessage(data.reply, "bot");
  } catch (e) {
    addMessage("Error contacting server.", "bot");
  }
}

sendBtn.addEventListener("click", send);
input.addEventListener("keydown", e => { if (e.key === "Enter") send(); });
