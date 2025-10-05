import React from "react";
import "./FloatingActionButton.css";

type FABProps = {
    label: string;
    onClick: () => void;
};

const FloatingActionButton: React.FC<FABProps> = ({ label, onClick }) => {
    return (
        <button className="fab" onClick={onClick}>
            {label}
        </button>
    );
};

export default FloatingActionButton;