import React from "react";
import "./Dialog.css";

type DialogProps = {
    isOpen: boolean;
    onClose: () => void;
    children: React.ReactNode;
};

const Dialog: React.FC<DialogProps> = ({ isOpen, onClose, children }) => {
    if (!isOpen) return null;
    return (
        <div className="dialog-backdrop">
            <div className="dialog-box">
                {children}
                <button onClick={onClose}>Close</button>
            </div>
        </div>
    );
};

export default Dialog;