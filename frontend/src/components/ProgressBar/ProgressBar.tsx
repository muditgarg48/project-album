import React from "react";
import "./ProgressBar.css";

type ProgressBarProps = {
    progress: number; // 0 to 100
};

const ProgressBar: React.FC<ProgressBarProps> = ({ progress }) => {
    return (
        <div className="progress-bar">
            <div className="progress" style={{ width: `${progress}%` }}></div>
        </div>
    );
};

export default ProgressBar;