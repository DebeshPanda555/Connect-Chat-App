// Connect with Flask-SocketIO integration
const socket = io(); // <-- connects to your Flask backend

(function () {
  const $ = (q, el = document) => el.querySelector(q);

  const els = {
    messages: $('#messages'),
    msgInput: $('#msgInput'),
    form: $('#composerForm'),
    typing: $('#typing'),
    chatName: $('#chatName'),
    chatStatus: $('#chatStatus'),
    clearBtn: $('#clearBtn'),
    newChatBtn: $('#newChatBtn'),
    attachBtn: $('#attachBtn'),
    themeBtn: $('#themeBtn'), // Added theme toggle button
  };

  // ------- events -------

  // Incoming messages
  socket.on("message", function (msg) {
    addMessage("in", msg);
  });

  // ------- DOM actions -------

  // Handle form submission (sending messages)
  els.form.addEventListener('submit', e => {
    e.preventDefault();
    sendMessage();
  });

  // Handle Reset button click
  els.clearBtn.addEventListener('click', () => {
    if (confirm("Are you sure you want to reset all data?")) {
      els.messages.innerHTML = ""; // Clear all messages
      els.chatStatus.textContent = "No messages";
      console.log("Data reset!");
    }
  });

  // Handle New Chat button click
  els.newChatBtn.addEventListener('click', () => {
    els.chatName.textContent = "New Chat";
    els.messages.innerHTML = ""; // Clear messages for the new chat
    els.chatStatus.textContent = "Start a new conversation!";
    console.log("New chat created!");
  });

  // Handle Attach button click
  els.attachBtn.addEventListener('click', () => {
    // Logic for handling attachments (demo)
    alert("Attachment feature is not implemented yet!");
    console.log("Attachment button clicked!");
  });

  // Handle Theme Toggle button click
  els.themeBtn.addEventListener('click', () => {
    const rootElement = document.documentElement;
    const isLight = rootElement.classList.toggle("light"); // Toggle the "light" class
    localStorage.setItem("theme", isLight ? "light" : "dark"); // Save the theme preference
    console.log(`Theme switched to ${isLight ? "light" : "dark"} mode`);
  });

  // Apply saved theme on page load
  const savedTheme = localStorage.getItem("theme");
  if (savedTheme) {
    document.documentElement.classList.toggle("light", savedTheme === "light");
  }

  // Message handling

  function sendMessage() {
    const txt = els.msgInput.value.trim();
    if (!txt) return;
    addMessage("out", txt); // Show immediately in UI
    socket.send(txt); // Send to Flask server
    els.msgInput.value = "";
  }

  function addMessage(role, text) {
    const row = document.createElement("div");
    row.className = `msg ${role}`;
    row.innerHTML = `
      <div class="bubble">${escapeHtml(text)}
        <div class="time">${timeStr(new Date())}</div>
      </div>`;
    els.messages.appendChild(row);
    els.messages.scrollTop = els.messages.scrollHeight;
    els.chatStatus.textContent = `${els.messages.children.length} message(s)`;
  }

  // Helpers 
  function escapeHtml(s) {
    return s.replace(/[&<>\"']/g, m => ({
      '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'
    }[m]));
  }

  function timeStr(d) {
    return d.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
  }
})();