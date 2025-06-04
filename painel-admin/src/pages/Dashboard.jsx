import Navbar from "../components/Navbar";
import Sidebar from "../components/Sidebar";

export default function Dashboard() {
  return (
    <div className="flex h-screen">
      <Sidebar />
      <div className="flex-1 flex flex-col">
        <Navbar />
        <main className="p-6">
          <h2 className="text-2xl font-bold mb-4">📊 Painel Administrativo</h2>
          <p className="text-gray-600">Aqui vai a gestão de imóveis, usuários e contratos.</p>
        </main>
      </div>
    </div>
  );
}
