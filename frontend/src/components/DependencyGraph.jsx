import React, {useEffect, useState} from "react";
import axios from "axios";
import API_BASE_URL from "../api";

export default function DependencyGraph(){

    const [graph,setGraph] = useState({});

    useEffect(()=>{
        axios.get(`${API_BASE_URL}/dependencies`)
        .then(res => setGraph(res.data))
    },[])

    return (
        <div style={{border:"1px solid #334155",padding:"20px",borderRadius:"10px"}}>
            <h2>Service Dependency Graph</h2>

            {Object.keys(graph).map(service => (
                <div key={service} style={{marginBottom:"20px"}}>
                    <h3>{service}</h3>

                    {graph[service].map(dep => (
                        <div key={dep} style={{marginLeft:"40px"}}>
                            ↳ {dep}
                        </div>
                    ))}
                </div>
            ))}
        </div>
    )
}