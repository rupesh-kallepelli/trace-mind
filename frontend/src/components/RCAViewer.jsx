import React, {useState} from "react";
import axios from "axios";
import API_BASE_URL from "../api";

export default function RCAViewer(){

    const [issue,setIssue] = useState("");
    const [result,setResult] = useState(null);

    const analyze = async () => {

        const response = await axios.post(
            `${API_BASE_URL}/analyze`,
            {issue}
        );

        setResult(response.data);
    }

    return (
        <div style={{border:"1px solid #334155",padding:"20px",borderRadius:"10px"}}>

            <h2>AI RCA Generator</h2>

            <input
                value={issue}
                onChange={(e)=>setIssue(e.target.value)}
                placeholder="payment failures after deployment"
                style={{
                    width:"70%",
                    padding:"10px",
                    borderRadius:"6px"
                }}
            />

            <button
                onClick={analyze}
                style={{
                    marginLeft:"10px",
                    padding:"10px 20px"
                }}
            >
                Analyze
            </button>

            {result && (
                <pre style={{
                    marginTop:"20px",
                    background:"#111827",
                    padding:"20px",
                    borderRadius:"10px",
                    overflow:"auto"
                }}>
                    {JSON.stringify(result,null,2)}
                </pre>
            )}
        </div>
    )
}