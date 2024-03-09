--
-- PostgreSQL database dump
--

-- Dumped from database version 16.2 (Ubuntu 16.2-1.pgdg22.04+1)
-- Dumped by pg_dump version 16.2 (Ubuntu 16.2-1.pgdg22.04+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: todo; Type: TABLE; Schema: public; Owner: John
--

CREATE TABLE public.todo (
    id integer NOT NULL,
    title character varying(80) NOT NULL,
    content text,
    completed boolean,
    created timestamp without time zone NOT NULL
);


ALTER TABLE public.todo OWNER TO "John";

--
-- Name: todo_id_seq; Type: SEQUENCE; Schema: public; Owner: John
--

CREATE SEQUENCE public.todo_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.todo_id_seq OWNER TO "John";

--
-- Name: todo_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: John
--

ALTER SEQUENCE public.todo_id_seq OWNED BY public.todo.id;


--
-- Name: todo id; Type: DEFAULT; Schema: public; Owner: John
--

ALTER TABLE ONLY public.todo ALTER COLUMN id SET DEFAULT nextval('public.todo_id_seq'::regclass);


--
-- Data for Name: todo; Type: TABLE DATA; Schema: public; Owner: John
--

COPY public.todo (id, title, content, completed, created) FROM stdin;
9	Complete Project	Finish the backend and frontend development	f	2024-03-09 07:32:43.295797
10	Exercise	Go for a 30-minute run	t	2024-03-09 07:33:02.568843
11	Read a Book	Read a chapter from your favorite book	f	2024-03-09 07:33:44.173629
13	Write Blog Post	Start drafting a new blog post	t	2024-03-09 07:34:08.062872
12	Update Project Status	Update the status of the ongoing project	f	2024-03-09 07:33:54.81503
\.


--
-- Name: todo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: John
--

SELECT pg_catalog.setval('public.todo_id_seq', 13, true);


--
-- Name: todo todo_pkey; Type: CONSTRAINT; Schema: public; Owner: John
--

ALTER TABLE ONLY public.todo
    ADD CONSTRAINT todo_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

