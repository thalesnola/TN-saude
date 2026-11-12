# Script deterministico para geracao de docs/diagrama-motion.svg
# Compativel 100% com sanitizador do GitHub (SVG Puro sem <filter> e sem style= inline)

import pathlib

SVG_CONTENT = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 920" width="1000" height="920">
  <defs>
    <!-- Degradê de fundo suave Motion -->
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#F3EEFF"/>
      <stop offset="50%" stop-color="#FFFFFF"/>
      <stop offset="100%" stop-color="#E9F7FF"/>
    </linearGradient>

    <!-- Ambient Glows em SVG Puro (substitui feGaussianBlur compatível com GitHub) -->
    <radialGradient id="glow_pink" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#FF7AC6" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#FF7AC6" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="glow_blue" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#2F9BFF" stop-opacity="0.22"/>
      <stop offset="100%" stop-color="#2F9BFF" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="glow_purple" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#8B5CF6" stop-opacity="0.18"/>
      <stop offset="100%" stop-color="#8B5CF6" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="glow_green" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#10B981" stop-opacity="0.20"/>
      <stop offset="100%" stop-color="#10B981" stop-opacity="0"/>
    </radialGradient>

    <!-- Motion Trails Diagonais -->
    <linearGradient id="trail_purple" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#8A5CF6" stop-opacity="0"/>
      <stop offset="50%" stop-color="#8A5CF6" stop-opacity="0.16"/>
      <stop offset="100%" stop-color="#8A5CF6" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="trail_blue" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#3B82F6" stop-opacity="0"/>
      <stop offset="50%" stop-color="#3B82F6" stop-opacity="0.14"/>
      <stop offset="100%" stop-color="#3B82F6" stop-opacity="0"/>
    </linearGradient>
  </defs>

  <!-- Fundo -->
  <rect width="1000" height="920" fill="url(#bg)"/>

  <!-- Ambient Glows -->
  <circle cx="910" cy="110" r="230" fill="url(#glow_pink)"/>
  <circle cx="90" cy="790" r="250" fill="url(#glow_blue)"/>
  <circle cx="500" cy="330" r="280" fill="url(#glow_purple)"/>

  <!-- Motion Trails Diagonais (-12deg) -->
  <rect x="120" y="80" width="280" height="26" rx="13" fill="url(#trail_purple)" transform="rotate(-12 260 93)"/>
  <rect x="680" y="440" width="260" height="24" rx="12" fill="url(#trail_blue)" transform="rotate(-12 810 452)"/>
  <rect x="60" y="36" width="406.5" height="26" rx="13" fill="#DCFCE7" stroke="#BBF7D0" stroke-width="1"/>
  <text x="263.25" y="53" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="11" font-weight="700" fill="#15803D" text-anchor="middle" letter-spacing="0.5">ACOMPANHAMENTO LONGITUDINAL · DADOS 100% SINTÉTICOS</text><text x="60" y="86" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="26" font-weight="800" fill="#1B1F3B">TN-saude · Hub Longitudinal de Saúde (Demonstração)</text><text x="60" y="114" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="14" font-weight="500" fill="#4A5568">Ingestão de exames, bioimpedâncias, antropometria e wearables em Registro Mestre com painéis locais.</text>
  <rect x="82" y="168" width="240" height="75" rx="14" fill="#1B1F3B" fill-opacity="0.06"/>
  <rect x="81" y="164" width="240" height="75" rx="14" fill="#1B1F3B" fill-opacity="0.05"/>
  <rect x="80" y="160" width="240" height="75" rx="14" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5"/><rect x="92" y="170" width="14" height="14" rx="7" fill="#EDE9FE"/><text x="114" y="182" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="12" font-weight="700" fill="#7C3AED">Antropometria Demo</text><text x="92" y="202" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="11" font-weight="400" fill="#475569"><tspan x="92" dy="0">Sessão: 76,5 kg · Σ7=76 mm</tspan><tspan x="92" dy="16">JP7: 11,9% · Navy: 16,5%</tspan></text><line x1="320" y1="197.5" x2="380" y2="290" stroke="#94A3B8" stroke-width="1.5" stroke-dasharray="3,3"/>
  <rect x="82" y="263" width="240" height="75" rx="14" fill="#1B1F3B" fill-opacity="0.06"/>
  <rect x="81" y="259" width="240" height="75" rx="14" fill="#1B1F3B" fill-opacity="0.05"/>
  <rect x="80" y="255" width="240" height="75" rx="14" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5"/><rect x="92" y="265" width="14" height="14" rx="7" fill="#E0F2FE"/><text x="114" y="277" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="12" font-weight="700" fill="#0284C7">Wearables Demo</text><text x="92" y="297" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="11" font-weight="400" fill="#475569"><tspan x="92" dy="0">FC Repouso: 58 bpm · Sono</tspan><tspan x="92" dy="16">Tendência estável sem ruído</tspan></text><line x1="320" y1="292.5" x2="380" y2="290" stroke="#94A3B8" stroke-width="1.5" stroke-dasharray="3,3"/>
  <rect x="82" y="358" width="240" height="75" rx="14" fill="#1B1F3B" fill-opacity="0.06"/>
  <rect x="81" y="354" width="240" height="75" rx="14" fill="#1B1F3B" fill-opacity="0.05"/>
  <rect x="80" y="350" width="240" height="75" rx="14" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5"/><rect x="92" y="360" width="14" height="14" rx="7" fill="#FEF3C7"/><text x="114" y="372" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="12" font-weight="700" fill="#D97706">Exames Laboratoriais</text><text x="92" y="392" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="11" font-weight="400" fill="#475569"><tspan x="92" dy="0">Glicemia: 88 · Perfil lipídico</tspan><tspan x="92" dy="16">Painel bioquímico em dia</tspan></text><line x1="320" y1="387.5" x2="380" y2="290" stroke="#94A3B8" stroke-width="1.5" stroke-dasharray="3,3"/>
  <rect x="382" y="198" width="240" height="200" rx="18" fill="#1B1F3B" fill-opacity="0.06"/>
  <rect x="381" y="194" width="240" height="200" rx="18" fill="#1B1F3B" fill-opacity="0.05"/>
  <rect x="380" y="190" width="240" height="200" rx="18" fill="#1B1F3B" stroke="#334155" stroke-width="1.5"/><rect x="400" y="206" width="130" height="20" rx="10" fill="#3B82F6"/><text x="465" y="220" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="10" font-weight="800" fill="#FFFFFF" text-anchor="middle">FONTE ÚNICA LOCAL</text><text x="400" y="248" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="14" font-weight="800" fill="#FFFFFF">Registro Mestre Demo</text><text x="400" y="272" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="11" font-weight="500" fill="#93C5FD"><tspan x="400" dy="0">• Atualização não-destrutiva</tspan><tspan x="400" dy="19">• Séries temporais em Markdown</tspan><tspan x="400" dy="19">• Regras e convenções estritas</tspan><tspan x="400" dy="19">• 100% de dados locais no disco</tspan><tspan x="400" dy="19">• Zero vazamento para nuvem</tspan></text><line x1="620" y1="290" x2="680" y2="290" stroke="#10B981" stroke-width="2.5"/><polygon points="680,285 690,290 680,295" fill="#10B981"/>
  <rect x="692" y="198" width="230" height="200" rx="18" fill="#1B1F3B" fill-opacity="0.06"/>
  <rect x="691" y="194" width="230" height="200" rx="18" fill="#1B1F3B" fill-opacity="0.05"/>
  <rect x="690" y="190" width="230" height="200" rx="18" fill="#FFFFFF" stroke="#86EFAC" stroke-width="1.5"/><rect x="706" y="206" width="125" height="20" rx="10" fill="#DCFCE7"/><text x="768" y="220" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="10" font-weight="800" fill="#16A34A" text-anchor="middle">SAÍDAS VISUAIS</text><text x="706" y="248" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="13" font-weight="700" fill="#1B1F3B">Painéis HTML Offline</text><text x="706" y="272" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="11" font-weight="400" fill="#475569"><tspan x="706" dy="0">• Gráficos de recomposição</tspan><tspan x="706" dy="19">• Curvas de tendência de peso</tspan><tspan x="706" dy="19">• Cruzamento de hábitos</tspan><tspan x="706" dy="19">• Relatórios para celular</tspan><tspan x="706" dy="19">• Visualização sem internet</tspan></text>
  <!-- BLOCO DE DEMONSTRAÇÃO PRÁTICA -->
  
  <rect x="62" y="563" width="880" height="220" rx="22" fill="#1B1F3B" fill-opacity="0.06"/>
  <rect x="61" y="559" width="880" height="220" rx="22" fill="#1B1F3B" fill-opacity="0.05"/>
  <rect x="60" y="555" width="880" height="220" rx="22" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
  
  <rect x="80" y="569" width="225" height="24" rx="12" fill="#1B1F3B"/>
  <text x="192" y="585" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="11" font-weight="800" fill="#60A5FA" text-anchor="middle" letter-spacing="0.8">DEMONSTRAÇÃO PRÁTICA</text>
  <text x="320" y="586" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="12" font-weight="600" fill="#64748B">Fluxo operacional concreto do repositório</text>
  
  <!-- Coluna 1: Entrada -->
  
  <rect x="84" y="613" width="260" height="155" rx="14" fill="#1B1F3B" fill-opacity="0.06"/>
  <rect x="83" y="609" width="260" height="155" rx="14" fill="#1B1F3B" fill-opacity="0.05"/>
  <rect x="82" y="605" width="260" height="155" rx="14" fill="#FFFFFF" stroke="#DDD6FE" stroke-width="1.5"/>
  <rect x="94" y="617" width="90" height="20" rx="10" fill="#EDE9FE"/>
  <text x="139" y="631" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="10" font-weight="800" fill="#7C3AED" text-anchor="middle">DADOS SINTÉTICOS</text>
  <text x="96" y="655" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="13" font-weight="700" fill="#1B1F3B">Sessão Mensal de Exemplo</text>
  <text x="96" y="675" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="11" font-weight="400" fill="#475569"><tspan x="96" dy="0">Perfil demo registra medições</tspan><tspan x="96" dy="16">de bioimpedância e dobras com</tspan><tspan x="96" dy="16">valores fictícios pré-calibrados.</tspan></text>
  
  <!-- Seta 1 -> 2 -->
  <circle cx="359" cy="682.5" r="14" fill="#EDE9FE" stroke="#C4B5FD" stroke-width="1.5"/>
  <text x="359" y="687.5" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="13" font-weight="800" fill="#7C3AED" text-anchor="middle">→</text>
  
  <!-- Coluna 2: Processamento -->
  
  <rect x="379" y="613" width="260" height="155" rx="14" fill="#1B1F3B" fill-opacity="0.06"/>
  <rect x="378" y="609" width="260" height="155" rx="14" fill="#1B1F3B" fill-opacity="0.05"/>
  <rect x="377" y="605" width="260" height="155" rx="14" fill="#FFFFFF" stroke="#BAE6FD" stroke-width="1.5"/>
  <rect x="389" y="617" width="125" height="20" rx="10" fill="#E0F2FE"/>
  <text x="451" y="631" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="10" font-weight="800" fill="#0284C7" text-anchor="middle">PROCESSAMENTO LOCAL</text>
  <text x="391" y="655" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="13" font-weight="700" fill="#1B1F3B">Cálculo e Versionamento</text>
  <text x="391" y="675" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="11" font-weight="400" fill="#475569"><tspan x="391" dy="0">Scripts calculam equações corporais,</tspan><tspan x="391" dy="16">atualizam o Registro_Mestre_Demo.md</tspan><tspan x="391" dy="16">e regeram os painéis de gráficos.</tspan></text>
  
  <!-- Seta 2 -> 3 -->
  <circle cx="654" cy="682.5" r="14" fill="#E0F2FE" stroke="#7DD3FC" stroke-width="1.5"/>
  <text x="654" y="687.5" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="13" font-weight="800" fill="#0284C7" text-anchor="middle">→</text>
  
  <!-- Coluna 3: Saída -->
  
  <rect x="674" y="613" width="260" height="155" rx="14" fill="#1B1F3B" fill-opacity="0.06"/>
  <rect x="673" y="609" width="260" height="155" rx="14" fill="#1B1F3B" fill-opacity="0.05"/>
  <rect x="672" y="605" width="260" height="155" rx="14" fill="#FFFFFF" stroke="#BBF7D0" stroke-width="1.5"/>
  <rect x="684" y="617" width="105" height="20" rx="10" fill="#DCFCE7"/>
  <text x="736" y="631" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="10" font-weight="800" fill="#16A34A" text-anchor="middle">PAINEL OFFLINE</text>
  <text x="686" y="655" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="13" font-weight="700" fill="#1B1F3B">Visualização Responsiva</text>
  <text x="686" y="675" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="11" font-weight="400" fill="#475569"><tspan x="686" dy="0">Gera Painel_Evolucao_Demo.html</tspan><tspan x="686" dy="16">interativo para consulta em tela</tspan><tspan x="686" dy="16">ou celular com sigilo absoluto.</tspan></text>
  <!-- Faixa Navy Inferior de Conclusão Técnica -->
  <rect x="60" y="800" width="880" height="64" rx="18" fill="#1B1F3B"/>
  <circle cx="95" cy="832" r="15" fill="#3B82F6" fill-opacity="0.25"/>
  <text x="95" y="837" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="15" font-weight="800" fill="#60A5FA" text-anchor="middle">✓</text>
  <text x="125" y="829" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="13" font-weight="800" fill="#FFFFFF">Dados 100% Sintéticos e Preservação Estrita de Privacidade</text>
  <text x="125" y="848" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="11" font-weight="500" fill="#94A3B8">Demonstração didática de governança de dados pessoais de saúde com processamento estritamente local.</text>
</svg>'''

def main():
    p = pathlib.Path(__file__).parent.parent / 'docs' / 'diagrama-motion.svg'
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(SVG_CONTENT, encoding='utf-8')
    print('SVG gerado em:', p)

if __name__ == '__main__':
    main()
