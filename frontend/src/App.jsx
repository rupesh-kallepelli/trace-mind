import React from "react";
import Dashboard from "./components/Dashboard";
import DependencyGraph from "./components/DependencyGraph";
import RCAViewer from "./components/RCAViewer";

export default function App() {
  return (
    <div style={{padding:"20px",fontFamily:"Arial",background:"#0f172a",minHeight:"100vh",color:"white"}}>
        <h1>ObservaAI Enterprise War Room</h1>

        <Dashboard />

        <div style={{marginTop:"30px"}}>
          <DependencyGraph />
        </div>

        <div style={{marginTop:"30px"}}>
          <RCAViewer />
        </div>
    </div>
  )
}