import React, { useState } from 'react';
import './FormCadAluno.css'; // Importe o arquivo CSS

const FormCadAluno = () => {
  const [formData, setFormData] = useState({
    fullName: '',
    ra: '',
    className: '',
    qrCode: '',
    nomeResponsavel:'',
    email: ''
  });

  const [submitMessage, setSubmitMessage] = useState(''); // Estado para a mensagem de envio

  const handleChange = (event) => {
    const { name, value } = event.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value
    }));
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    console.log('handleSubmit foi chamada!');

    try {
      console.log('Enviando:', formData);

      const response = await fetch('http://localhost:5000/addStudent', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
      });

      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }

      const result = await response.json();
      console.log(result);

      // Defina a mensagem com base na resposta da solicitação
      setSubmitMessage('Cadastrado com sucesso');
    } catch (error) {
      console.error('Erro ao enviar os dados', error);

      // Em caso de erro, defina a mensagem de erro
      setSubmitMessage('Erro ao cadastrar');
    }
  };

  return (
    <div>
      <form className="form-container" onSubmit={handleSubmit}>
        {/* Se houver uma mensagem de envio, exiba-a */}
        {submitMessage && <p className={submitMessage === 'Erro ao cadastrar' ? 'error' : 'success'}>{submitMessage}</p>}
        <div className="form-group">
          <label htmlFor="fullName">Nome completo:</label>
          <input
            type="text"
            name="fullName"
            id="fullName"
            value={formData.fullName}
            onChange={handleChange}
          />
        </div>
        <div className="form-group">
          <label htmlFor="ra">RA:</label>
          <input type="text" name="ra" id="ra" value={formData.ra} onChange={handleChange} />
        </div>
        <div className="form-group">
          <label htmlFor="className">Turma:</label>
          <input
            type="text"
            name="className"
            id="className"
            value={formData.className}
            onChange={handleChange}
          />
        </div>
        <div className="form-group">
          <label htmlFor="qrCode">QR Carteirinha:</label>
          <input
            type="text"
            name="qrCode"
            id="qrCode"
            value={formData.qrCode}
            onChange={handleChange}
          />
        </div>
        <div className="form-group">
          <label htmlFor="nomeResponsavel">Nome do Responsável:</label>
          <input
            type="text"
            name="nomeResponsavel"
            id="nomeResponsavel"
            value={formData.nomeResponsavel}
            onChange={handleChange}
          />
        </div>
        <div className="form-group">
          <label htmlFor="email">E-mail do Responsável:</label>
          <input
            type="text"
            name="email"
            id="email"
            value={formData.email}
            onChange={handleChange}
          />
        </div>
        <button type="submit">Enviar</button>
      </form>
    </div>
  );
};

export default FormCadAluno;
