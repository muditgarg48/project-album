import { createSlice } from "@reduxjs/toolkit";

interface UIState {
    dialogOpen: boolean;
}


const initialState: UIState = {
    dialogOpen: false,
};


const uiSlice = createSlice({
    name: "ui",
    initialState,
    reducers: {
        openDialog: (state) => {
            state.dialogOpen = true;
        },  
        closeDialog: (state) => {
            state.dialogOpen = false;
        },
    },
});


export const { openDialog, closeDialog } = uiSlice.actions;
export default uiSlice.reducer;