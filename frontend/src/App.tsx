import React, { useState } from "react";
import "./App.css";
import SearchBar from "./components/SearchBar/SearchBar.tsx";
import FloatingActionButton from "./components/FloatingActionButton/FloatingActionButton.tsx";
import Time from "./tabs/Time/Time.tsx";
import Location from "./tabs/Location/Location.tsx";
import Device from "./tabs/Device/Device.tsx";
import FileType from "./tabs/FileType/FileType.tsx";
import Properties from "./tabs/Properties/Properties.tsx";

const tabs = ["Time", "Location", "Device", "FileType", "Properties"];

function App() {
    const [activeTab, setActiveTab] = useState("Time");

    const renderTab = () => {
        switch (activeTab) {
            case "Time":
                return <Time />;
            case "Location":
                return <Location />;
            case "Device":
                return <Device />;
            case "FileType":
                return <FileType />;
            case "Properties":
                return <Properties />;
            default:
                return null;
        }
    };

    return (
        <div>
            <SearchBar />
            <div style={{ display: "flex", justifyContent: "center", margin: "1rem 0" }}>
                {tabs.map((tab) => (
                    <div
                        key={tab}
                        onClick={() => setActiveTab(tab)}
                        style={{
                        cursor: "pointer",
                        margin: "0 1rem",
                        padding: "0.5rem 1rem",
                        borderRadius: activeTab === tab ? "var(--button-radius)" : "0",
                        backgroundColor: activeTab === tab ? "var(--button-color)" : "transparent",
                        color: activeTab === tab ? "var(--button-text-color)" : "var(--secondary-text-color)",
                        boxShadow: activeTab === tab ? "0 2px 6px rgba(0,0,0,0.2)" : "none",
                        fontSize: "var(--tab-font-size)",
                        }}
                    >
                        {tab}
                    </div>
                ))}
            </div>
            <div style={{ padding: "1rem" }}>{renderTab()}</div>
            <FloatingActionButton label="+" onClick={() => alert("Add Folder clicked")}/>
        </div>
    );
}

export default App;