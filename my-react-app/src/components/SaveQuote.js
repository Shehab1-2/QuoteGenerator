import React from 'react';

function SaveQuote({ saveQuote }) {
    return (
        <button onClick={saveQuote}>
            Save
        </button>
    );
}

export default SaveQuote;
