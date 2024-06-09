import { Routes, Route } from "react-router-dom";
import { LoginPage } from "./pages/Login";
import { HomePage } from "./pages/Home";

import "./App.css";
import { ProtectedRoute } from "./components/ProtectedRoute";
import { AuthProvider } from "./hooks/useAuth";

function App() {
  return (
    <AuthProvider>
      <Routes>
        <Route element={<ProtectedRoute/>}>
          <Route path="/" element={<HomePage />} />
        </Route>
        <Route path="/login" element={<LoginPage />} />
      </Routes>
    </AuthProvider>
  );
}

export default App;
