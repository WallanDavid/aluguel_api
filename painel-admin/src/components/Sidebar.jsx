import { Link } from "react-router-dom";

export default function Sidebar() {
  return (
    <aside className="w-64 h-full bg-gray-100 border-r px-4 py-6 hidden md:block">
      <nav className="space-y-4">
        <Link to="/dashboard" className="block font-medium text-gray-700 hover:text-blue-600">📊 Dashboard</Link>
        <Link to="/usuarios" className="block font-medium text-gray-700 hover:text-blue-600">👥 Usuários</Link>
        <Link to="/imoveis" className="block font-medium text-gray-700 hover:text-blue-600">🏢 Imóveis</Link>
        <Link to="/contratos" className="block font-medium text-gray-700 hover:text-blue-600">📄 Contratos</Link>
        <Link to="/login" className="block font-medium text-red-500 hover:text-red-700">🚪 Sair</Link>
      </nav>
    </aside>
  );
}
