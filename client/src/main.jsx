import React from "react";
import ReactDOM from "react-dom/client";
import "@/styles/index.css";
import { BrowserRouter as Router } from "react-router-dom";
import { useRoutesWith404 } from "@/lib/hooks/hooks";
import routes from "~react-pages";
import { AuthProvider } from "@/context/AuthContext";
import Header from "@/components/Header";

const App = () => {
  const element = useRoutesWith404(routes);
  return <div className="">{element}</div>;
};

ReactDOM.createRoot(document.getElementById("root")).render(
  <>
    <Router>
      <AuthProvider>
        <Header/>
        <App />
      </AuthProvider>
    </Router>
  </>
);
