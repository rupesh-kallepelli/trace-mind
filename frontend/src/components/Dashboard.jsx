import React, { useEffect, useState } from "react";
import axios from "axios";
import API_BASE_URL from "../api";

export default function Dashboard() {

  const [summary, setSummary] = useState({});
  const [incidents, setIncidents] = useState([]);

  useEffect(() => {
    axios.get(`${API_BASE_URL}/dashboard/summary`)
      .then(res => setSummary(res.data));

    axios.get(`${API_BASE_URL}/dashboard/incidents`)
      .then(res => setIncidents(res.data));
  }, []);

  return (
    <div>
      <div style={{
        display: "grid",
        gridTemplateColumns: "repeat(4, 1fr)",
        gap: "15px"
      }}>
        <Card title="Active Incidents" value={summary.active_incidents} />
        <Card title="Healthy Services" value={summary.healthy_services} />
        <Card title="Critical Services" value={summary.critical_services} />
        <Card title="Cluster Health" value={summary.cluster_health} />
      </div>

      <h2 style={{marginTop: "30px"}}>Incidents</h2>

      <table border="1" cellPadding="10">
        <thead>
          <tr>
            <th>ID</th>
            <th>Service</th>
            <th>Severity</th>
            <th>Status</th>
          </tr>
        </thead>
        <tbody>
          {incidents.map(i => (
            <tr key={i.id}>
              <td>{i.id}</td>
              <td>{i.service}</td>
              <td>{i.severity}</td>
              <td>{i.status}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

function Card({title, value}) {
  return (
    <div style={{
      border: "1px solid #ccc",
      borderRadius: "10px",
      padding: "20px"
    }}>
      <h3>{title}</h3>
      <h2>{value}</h2>
    </div>
  );
}