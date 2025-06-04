import Navbar from "../components/Navbar";
import Sidebar from "../components/Sidebar";

export default function Imoveis() {
  return (
    <div className="flex h-screen">
      <Sidebar />
      <div className="flex-1 flex flex-col">
        <Navbar />
        <main className="p-6">
          <h2 className="text-xl font-bold mb-4">🏢 Gestão de Imóveis</h2>
          <p className="text-gray-600">Aqui você poderá listar, cadastrar e alterar imóveis.</p>
        </main>
      </div>
    </div>
  );
}
