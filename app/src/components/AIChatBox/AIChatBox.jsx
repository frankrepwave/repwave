import React, { useState } from 'react';
import './AIChatBox.css'; 

const AIChatBox = () => {
  const [inputValue, setInputValue] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault(); 
    alert(inputValue); 
  };

  const handleChange = (event) => {
    setInputValue(event.target.value);
  };

  return (
    <form onSubmit={handleSubmit}>
      <div className="input-container">
        <p className='prompt-question'>Do you want more info?</p>
      <textarea
        value={inputValue}
        onChange={handleChange}
        placeholder="Ask our AI in this chat box for more details or certain format changes.
Can even ask it to make a specific list or export a csv of deals discussed!"
        className="text-input"
        />
        <p className='disclaimer'>This will cost 1 Repwave Token</p>
      </div>

      <div className="submit-container">
        <button type="submit" className="submit-button">
          Submit
        </button>
      </div>
    </form>
  );
};

export default AIChatBox;
