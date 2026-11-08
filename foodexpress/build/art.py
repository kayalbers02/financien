"""Geanimeerde eten-tekeningen per Foodexpress-categorie-id (SVG-inhoud, viewBox 0 0 120 120)."""

KAPSALON = '''<g stroke="#B7A27F" stroke-width="3" fill="none" stroke-linecap="round"><path class="st" d="M48 40 q-5-8 0-16 q5-8 0-16"/><path class="st st2" d="M72 40 q-5-8 0-16 q5-8 0-16"/></g>
<path d="M14 70 L106 70 L98 104 L22 104 Z" fill="#C9CED3"/><path d="M14 70 L106 70 L104 76 L16 76 Z" fill="#AEB4BA"/>
<rect x="24" y="58" width="72" height="14" rx="5" fill="#F6C33B"/>
<g fill="#8A4B23"><rect x="28" y="54" width="18" height="8" rx="4"/><rect x="50" y="52" width="20" height="9" rx="4"/><rect x="74" y="54" width="18" height="8" rx="4"/></g>
<path class="melt" d="M24 52 h72 v6 q-6 10-10 0 q-6 12-12 0 q-6 10-12 0 q-6 12-12 0 q-6 10-12 0 q-6 12-14 0 Z" fill="#FFE07A"/>
<g fill="#4FAE5A"><circle cx="34" cy="48" r="5"/><circle cx="58" cy="46" r="5"/><circle cx="84" cy="48" r="5"/></g>
<g fill="#E8473B"><circle cx="46" cy="47" r="4"/><circle cx="72" cy="46" r="4"/></g>'''

ART = {
 6: KAPSALON,
 1: '''<circle cx="60" cy="68" r="44" fill="#E3A24F"/><circle cx="60" cy="68" r="37" fill="#F2C94C"/>
<g fill="#C8322A"><circle cx="44" cy="58" r="6"/><circle cx="72" cy="82" r="6"/><circle cx="46" cy="86" r="5"/></g>
<rect class="string" x="68" y="44" width="3" height="20" rx="1.5" fill="#FBE08A"/><rect class="string" x="76" y="50" width="3" height="16" rx="1.5" fill="#FBE08A"/>
<g class="slice"><path d="M60 68 L60 24 A44 44 0 0 1 98 46 Z" fill="#E3A24F"/><path d="M60 68 L60 31 A37 37 0 0 1 92 49.5 Z" fill="#F2C94C"/><circle cx="72" cy="48" r="5" fill="#C8322A"/></g>''',
 4: '''<rect class="layer" x="22" y="90" width="76" height="14" rx="7" fill="#E0A04B"/>
<rect class="layer l2" x="20" y="78" width="80" height="14" rx="7" fill="#6B3A1E"/>
<path class="layer l3" d="M20 76 h80 l-6 8 l-8-6 l-8 8 l-8-8 l-8 8 l-8-8 l-8 8 l-8-8 l-8 6 Z" fill="#F7C531"/>
<path class="layer l4" d="M18 70 q8-6 14 0 q8-6 14 0 q8-6 14 0 q8-6 14 0 q8-6 14 0 q8-6 14 0 v4 h-84 Z" fill="#4FAE5A"/>
<g class="layer l5"><path d="M22 68 q0-36 38-36 q38 0 38 36 Z" fill="#E7A24C"/><g fill="#FFF3D1"><ellipse cx="44" cy="46" rx="3" ry="1.6"/><ellipse cx="60" cy="40" rx="3" ry="1.6"/><ellipse cx="76" cy="48" rx="3" ry="1.6"/><ellipse cx="54" cy="54" rx="3" ry="1.6"/></g></g>''',
 11: '''<g stroke="#B7A27F" stroke-width="3" fill="none" stroke-linecap="round"><path class="st" d="M40 44 q-5-8 0-16 q5-8 0-16"/><path class="st st2" d="M60 40 q-5-8 0-16 q5-8 0-16"/><path class="st st3" d="M80 44 q-5-8 0-16 q5-8 0-16"/></g>
<g class="siz"><rect x="18" y="60" width="84" height="20" rx="10" fill="#8A4B23"/><rect x="18" y="60" width="84" height="7" rx="3.5" fill="#A55E2E"/><rect x="30" y="84" width="60" height="22" rx="11" fill="#C27A35"/><g fill="#9A5B22"><circle cx="42" cy="92" r="1.6"/><circle cx="52" cy="98" r="1.6"/><circle cx="64" cy="91" r="1.6"/><circle cx="76" cy="97" r="1.6"/></g></g>''',
 12: '''<g fill="#F6C33B" stroke="#C98A12" stroke-width="2"><rect class="f1" x="34" y="22" width="9" height="52" rx="3"/><rect class="f2" x="45" y="14" width="9" height="60" rx="3"/><rect class="f3" x="56" y="18" width="9" height="56" rx="3"/><rect class="f4" x="67" y="12" width="9" height="62" rx="3"/><rect class="f5" x="78" y="24" width="9" height="50" rx="3"/></g>
<path d="M28 56 L92 56 L84 108 L36 108 Z" fill="#D9261C"/><path d="M28 56 L92 56 L90 66 L30 66 Z" fill="#B51E15"/><ellipse cx="60" cy="86" rx="12" ry="8" fill="#FFFFFF"/><path d="M54 86 h12" stroke="#D9261C" stroke-width="3" stroke-linecap="round"/>''',
 21: '''<g stroke="#B7A27F" stroke-width="3" fill="none" stroke-linecap="round"><path class="st" d="M52 30 q-5-8 0-16 q5-8 0-16"/><path class="st st2" d="M70 28 q-5-8 0-16 q5-8 0-16"/></g>
<g class="tilt"><path d="M36 44 Q60 30 84 44 L76 110 Q60 116 44 110 Z" fill="#EBC789"/><g class="bob"><circle cx="46" cy="42" r="7" fill="#4FAE5A"/></g><g class="bob bob2"><rect x="54" y="32" width="14" height="10" rx="4" fill="#8A4B23"/></g><g class="bob bob3"><circle cx="74" cy="42" r="6" fill="#E8473B"/></g>
<path d="M36 44 Q60 54 84 44 L82 58 Q60 66 38 58 Z" fill="#DDB271"/><path d="M42 80 Q60 86 78 80 L76 110 Q60 116 44 110 Z" fill="#C9CED3"/><path d="M42 80 Q60 86 78 80 L77.5 85 Q60 91 42.5 85 Z" fill="#AEB4BA"/></g>''',
 13: '''<rect x="64" y="10" width="6" height="40" rx="3" fill="#D9261C" transform="rotate(14 67 30)"/><path d="M32 34 L88 34 L80 108 L40 108 Z" fill="#E4F2FA" stroke="#9CC3D8" stroke-width="2"/><path d="M35 50 L85 50 L80 106 L40 106 Z" fill="#6B2E1B"/>
<g fill="#C9876A"><circle class="bb" cx="50" cy="96" r="3"/><circle class="bb bb2" cx="62" cy="100" r="2.5"/><circle class="bb bb3" cx="72" cy="94" r="3"/></g><rect x="28" y="28" width="64" height="8" rx="4" fill="#9CC3D8"/>''',
 25: '''<path d="M40 62 L80 62 L60 112 Z" fill="#D9A55A"/><g stroke="#B9843B" stroke-width="2"><path d="M46 70 L70 96"/><path d="M58 64 L76 82"/><path d="M74 70 L52 96"/><path d="M62 64 L44 82"/></g>
<circle cx="60" cy="34" r="17" fill="#F6B8C8"/><circle cx="48" cy="54" r="15" fill="#6B3A1E"/><circle cx="72" cy="54" r="15" fill="#FFF3DC"/>
<rect class="drip" x="44" y="62" width="6" height="14" rx="3" fill="#6B3A1E"/><rect class="drip drip2" x="74" y="62" width="6" height="12" rx="3" fill="#FFF3DC"/>
<g class="bob"><rect x="54" y="20" width="3" height="8" rx="1.5" fill="#4FAE5A" transform="rotate(30 55 24)"/></g><g class="bob bob2"><rect x="64" y="26" width="3" height="8" rx="1.5" fill="#F6C33B" transform="rotate(-25 65 30)"/></g><g class="bob bob3"><rect x="58" y="36" width="3" height="8" rx="1.5" fill="#D9261C" transform="rotate(70 59 40)"/></g>''',
}
