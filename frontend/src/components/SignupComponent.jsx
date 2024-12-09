import { React, useEffect, useState } from 'react';
import { LockOutlined, UserOutlined, MailOutlined } from '@ant-design/icons';
import { Button, Form, Input} from 'antd';
import Image from '../public/images/logo.png';
import axios from 'axios';
import Cookies from 'js-cookie';
import { useNavigate } from "react-router-dom";

const SignupForm = () => {

  const navigate = useNavigate();

  const signupRequest = (data) => {
    axios.post('http://127.0.0.1:5000/users/signup',
      data = data,
      ).then(r => {
        navigate('/');
    })
    .catch(function (error) {
      console.log(error);
    });
  }

  const onFinish = (values) => {
    signupRequest(values)
  }; 

  return (
    
    <Form
      style={{
        textAlign: "center",
        padding: '0 48px'
      }}
      name="login"
      initialValues={{
        remember: true,
      }}
      onFinish={onFinish}
    >

      <a href='/'>
      <img 
        src={Image}
        width={125}
        height={125}
      ></img>
      </a>
    
      <h1>Signup</h1>

      <Form.Item
        name="username"
        rules={[
          {
            required: true,
            message: 'Please input your Username!',
          },
        ]}
      >
        <Input prefix={<UserOutlined />} placeholder="Username" />
      </Form.Item>

      <Form.Item
        name="email"
        rules={[
          {
            required: true,
            message: 'Please input your Email!',
          },
        ]}
      >
        <Input prefix={<MailOutlined />} placeholder="Email" />
      </Form.Item>

      <Form.Item
        name="password"
        rules={[
          {
            required: true,
            message: 'Please input your Password!',
          },
        ]}
      >
        <Input prefix={<LockOutlined />} type="password" placeholder="Password" />
      </Form.Item>

      <Form.Item>
        <Button block type="primary" htmlType="submit">
          Sign up
        </Button>
        or <a href="/#login">Login now!</a>
      </Form.Item>
    </Form>
  );
};
export default SignupForm;