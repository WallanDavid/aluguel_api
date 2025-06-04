import { execSync } from "child_process";
import { writeFileSync, mkdirSync } from "fs";
import path from "path";

const run = (cmd) => execSync(cmd, { stdio: "inherit" });

console.log("🚀 Criando projeto Vite + React...");
run("npm create vite@latest painel-admin -- --template react");
process.chdir("painel-admin");

console.log("📦 Instalando dependências...");
run("npm install");
run("npm install -D tailwindcss postcss autoprefixer");
run("npm install axios react-router-dom react-toastify");

console.log("🛠️ Configurando Tailwind...");
run("npx tailwindcss init -p");

// tailwind.config.js
writeFileSync("tailwind.config.js", `/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {},
  },
  plugins: [],
}`);

// postcss.config.js
writeFileSync("postcss.config.js", `export default {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}`);

// index.css
writeFileSync("src/index.css", `@tailwind base;
@tailwind components;
@tailwind utilities;
`);

// api.js
mkdirSync("src/services", { recursive: true });
writeFileSync("src/services/api.js", `import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:8000", // Altere conforme necessário
});

api.interceptors.request.use((config) => {
  const token = localStorage.getItem("token");
  if (token) config.headers.Authorization = \`Bearer \${token}\`;
  return config;
});

export default api;
`);

// Login.jsx
mkdirSync("src/pages", { recursive: true });
writeFileSync("src/pages/Login.jsx", `import { useState } from "react";
import api from "../services/api";
import { useNavigate } from "react-router-dom";

export default function Login() {
  const [email, setEmail] = useState("");
  const [senha, setSenha] = useState("");
  const navigate = useNavigate();

  const handleLogin = async () => {
    try {
      const res = await api.post("/login", new URLSearchParams({ username: email, password: senha }));
      localStorage.setItem("token", res.data.access_token);
      navigate("/dashboard");
    } catch (err) {
      alert("Erro ao fazer login");
    }
  };

  return (
    <div className="flex flex-col items-center justify-center h-screen gap-4">
      <h1 className="text-2xl font-bold">Login Admin</h1>
      <input type="email" placeholder="Email" className="border p-2" onChange={(e) => setEmail(e.target.value)} />
      <input type="password" placeholder="Senha" className="border p-2" onChange={(e) => setSenha(e.target.value)} />
      <button onClick={handleLogin} className="bg-blue-600 text-white px-4 py-2">Entrar</button>
    </div>
  );
}`);

// Dashboard.jsx
writeFileSync("src/pages/Dashboard.jsx", `import { useEffect, useState } from "react";
import api from "../services/api";

export default function Dashboard() {
  const [imoveis, setImoveis] = useState([]);

  useEffect(() => {
    api.get("/imoveis").then((res) => setImoveis(res.data));
  }, []);

  return (
    <div className="p-4">
      <h1 className="text-xl font-bold mb-4">Imóveis</h1>
      <ul>
        {imoveis.map((i) => (
          <li key={i.id}>{i.endereco} - R$ {i.valor}</li>
        ))}
      </ul>
    </div>
  );
}
`);

// App.jsx
writeFileSync("src/App.jsx", `import { BrowserRouter, Routes, Route } from "react-router-dom";
import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/dashboard" element={<Dashboard />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
`);

console.log("✅ Projeto pronto! Rode: cd painel-admin && npm run dev");
