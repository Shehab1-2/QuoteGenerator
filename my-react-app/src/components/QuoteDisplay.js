import React from 'react';

function QuoteDisplay({ quote }) {
    return (
        <div className="quote-display">
            <p className="quote">"{quote.quote}"</p>
            <p className="author">- {quote.author}</p>
        </div>
    );
}

export default QuoteDisplay;
