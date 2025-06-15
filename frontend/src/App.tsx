import React, { useEffect, useState } from 'react';
import io from 'socket.io-client';

function App() {
  const [messages, setMessages] = useState<string[]>([]);

  useEffect(() => {
    const socket = io('http://localhost:5000');

    socket.on('connect', () => {
      console.log('Connected to server');
    });

    socket.on('message', (data: any) => {
      setMessages((prev) => [...prev, JSON.stringify(data)]);
    });

    return () => {
      socket.disconnect();
    };
  }, []);

  return (
    <div>
      <h1>WebSocket Demo</h1>
      <ul>
        {messages.map((msg, idx) => (
          <li key={idx}>{msg}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
