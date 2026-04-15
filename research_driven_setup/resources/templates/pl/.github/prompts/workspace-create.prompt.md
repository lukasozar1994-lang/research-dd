<!-- user-language: pl -->

# Cel:
Przygotowanie pełnej analizy i raportu badawczego dotyczącego best practices w zakresie budowy gotowych instalatorów framworków dla agentów ai, podobnych do "Spec-kit" od Githuba które pozwalają na szybkie i łatwe przygotowanie środowisko do pracy w odpowiednim workflow.
# Kontekst:
Buduje pełny workflow do zadań produkcyjnych, ma on działać w oparciu o kolejne kroki:
1. Dogłębna analiza tematu i zbieranie danych przez agentów badawczych:
  - `.github/agents/deep_research.agent.md` - agent który zbiera dane z internetu, dokumentacji, badań naukowych, forów, itp. i przygotowuje z nich raport badawczy.
  - `.github/agents/context7.agent.md` - agent który jest ekspertem w zakresie stacków technologicznych, bibliotek, frameworków, itp. przygotowuje raporty i analzizy konretnych technologii, ich zalet, wad, porównań, itp.
2. Na podstawie raportów badawczych, agent planujący (`.github/agents/plan_architect.agent.md`) przygotowuje szczegółowy plan implementacji, który zawiera całą masę artefaktów takich jak: intake, gap analysis, konstytucja projektu, specyfikacja techniczna, stack technologiczny, architektura i mapa plików, plan implementacji, task breakdown, kryteria akceptacji, plan testów, readiness review, ryzyka i zależności.
3. Na podstawie planu implementacji, mam już agenta który wykonuje pełną implementacje projektu `.github/agents/implement_worker.agent.md`., który jest w stanie przeprowadzić pełen proces implementacji, od przygotowania środowiska, przez implementacje, aż po testy i stabilizację.
4. Dodatkowow stowrzyłem sobie agenta do debugowania problemów z frontendem, który wykorzystuje `playwright-cli` do automatyzacji interakcji z przeglądarką i debugowania aplikacji webowych `.github/agents/playwright-debug.agent.md`.
5. Dodatkowo mam agenta do tworzenia gotowych scenariuszy testowych, dla agenta `playwright-debug.agent.md` który jest w stanie na podstawie zadań określonych przez programiste przygotować gotowe scenariusze testowe, które można łatwo uruchomić w `playwright-cli` `.github/agents/test-scenario-architect.agent.md`.

# Zadanie:
Chciałbym żebyś przeprowadził pełną analizę tematu i przygotował raport badawczy dotyczący best practices w zakresie budowy gotowych instalatorów framworków dla agentów ai, podobnych do "Spec-kit" od Githuba które pozwalają na szybkie i łatwe przygotowanie środowisko do pracy w odpowiednim workflow. Raport powinien zawierać:
1. Przegląd istniejących rozwiązań i narzędzi w tym zakresie, takich jak "Spec-kit" od Githuba, oraz innych podobnych narzędzi i frameworków.
2. Jak zbudowac instalator frameworka, pwoedzmy że chciałbym umieścić to w formie gotowego projektu na Githubie, który będzie zawierał wszystkie potrzebne pliki, skrypty, dokumentację, itp. do łatwego i szybkiego przygotowania środowiska do pracy z agentami ai.
3. Jeżeli już bede miał wszystkich moich agentów, skille, skrypty, itp. gotowe, to jak zbudować z tego gotowy instalator frameworka, który będzie łatwy w użyciu, bedzie od razu pobierał wszystko z githuba oraz instalował wszystkie potrzebne zależności, oraz instalował i konfigurował serwery MCP dla agetnów z których korzystam.
4. Jak później uruchomić taki instalator, pracuje w vs code i dla vs code oraz github copilot chat ma być ten framework, oraz głównie dla linuxa, w którym głównie pracuje czyli dla ubuntu.
