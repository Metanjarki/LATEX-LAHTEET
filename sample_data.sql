COPY lahteet.source (source_id, bibtex_key, kind, title, year, author, note) FROM stdin;
173	ritchie88	book	The C programming language	1988	D. Ritchie, B. Kernighan	\N
174	ostep	book	Operating Systems: Three Easy Pieces	2012	Remzi H. Arpaci-Dusseau, Andrea C. Arpaci-Dusseau	\N
175	turing	article	I.—COMPUTING MACHINERY AND INTELLIGENCE	1950	TURING, A. M.	\N
176	weiser	article	Some computer science issues in ubiquitous computing	1993	Weiser, Mark	\N
177	deepresidual	inproceedings	Deep Residual Learning for Image Recognition	2015	Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun	\N
\.


--
-- Data for Name: source_article; Type: TABLE DATA; Schema: lahteet; Owner: tatu
--

COPY lahteet.source_article (source_article_id, source_id, journal, volume, number, pages, month) FROM stdin;
39	175	Mind	59	236	433-460	10
40	176	Communications of the ACM	36	7	75--84	
\.


--
-- Data for Name: source_book; Type: TABLE DATA; Schema: lahteet; Owner: tatu
--

COPY lahteet.source_book (source_book_id, source_id, publisher, editor, volume, number, series, address, edition, month, note) FROM stdin;
111	173	Bell Laboratories	\N	\N	\N	\N	\N	\N	\N	\N
112	174	\t CreateSpace Independent Publishing Platform	\N	\N	\N	\N	\N	\N	\N	\N
\.


--
-- Data for Name: source_inproceedings; Type: TABLE DATA; Schema: lahteet; Owner: tatu
--

COPY lahteet.source_inproceedings (source_inproceedings_id, source_id, booktitle, editor, series, pages, address, month, organization, publisher, volume) FROM stdin;
25	177	Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR)	Markus Arnold and Jenny Lee	CVPR Proceedings	770--778	Las Vegas, NV, USA	June	IEEE	IEEE	1
\.


--
-- Data for Name: tag; Type: TABLE DATA; Schema: lahteet; Owner: tatu
--

COPY lahteet.tag (tag_id, source_id, name) FROM stdin;
91	173	Paksu kirja
92	174	Mielenkiintoinen
93	174	Luettu
94	173	Haluan lukea
95	176	Roskakoriin 💩
96	175	Vanha
97	177	ChatGPT:ltä saatu
\.

