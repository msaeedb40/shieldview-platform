import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { GlassCardComponent } from '../shared/glass-card.component';
import { ThreatTableComponent } from '../shared/threat-table.component';

@Component({
    selector: 'app-dashboard-overview',
    standalone: true,
    imports: [CommonModule, GlassCardComponent, ThreatTableComponent],
    template: `
    <div class="dashboard-container">
      <header class="top-nav">
        <div class="logo">SHIELD<span>VIEW</span></div>
        <div class="user-profile">Analyst Admin</div>
      </header>

      <div class="grid-layout">
        <div class="hero-map">
          <app-glass-card title="Global Threat Map (Real-time)">
            <div id="three-js-canvas" class="map-placeholder">
              <div class="mapping-overlay">
                <div class="pulse"></div>
                <span>Scanning 3D Vector Space...</span>
              </div>
            </div>
          </app-glass-card>
        </div>

        <div class="stat-sidebar">
          <app-glass-card title="Active Threats">
            <h1 class="big-number">1,248</h1>
            <p class="trend up">+12% from last hour</p>
          </app-glass-card>
          
          <app-glass-card title="System Health">
            <div class="health-indicator">Secure</div>
          </app-glass-card>
        </div>

        <div class="full-width">
          <app-glass-card title="Recent Security Events">
            <app-threat-table [threats]="mockThreats"></app-threat-table>
          </app-glass-card>
        </div>
      </div>
    </div>
  `,
    styles: [`
    .dashboard-container { padding: 2rem; background: #050505; min-height: 100vh; }
    .top-nav { display: flex; justify-content: space-between; margin-bottom: 2rem; }
    .logo { font-size: 1.5rem; font-weight: bold; }
    .logo span { color: #00f2ff; }
    .grid-layout { display: grid; grid-template-columns: 2fr 1fr; gap: 2rem; }
    .hero-map { height: 500px; }
    .map-placeholder { height: 400px; background: rgba(255,255,255,0.02); display: flex; align-items: center; justify-content: center; position: relative; overflow: hidden; }
    .full-width { grid-column: 1 / span 2; }
    .big-number { font-size: 3rem; margin: 0; color: #00f2ff; }
    .health-indicator { color: #00ff88; font-weight: bold; font-size: 1.2rem; }
    .mapping-overlay { text-align: center; }
    .pulse { width: 100px; height: 100px; border: 2px solid #00f2ff; border-radius: 50%; margin: 0 auto 1rem; animation: pulse 2s infinite; }
    @keyframes pulse { 0% { transform: scale(0.5); opacity: 1; } 100% { transform: scale(1.5); opacity: 0; } }
  `]
})
export class DashboardOverviewComponent implements OnInit {
    mockThreats = [
        { ip: '192.168.1.105', type: 'SQL Injection', severity: 'Critical', status: 'Blocked', time: '2 mins ago' },
        { ip: '45.12.33.101', type: 'DDoS Attack', severity: 'High', status: 'Mitigating', time: '5 mins ago' },
        { ip: '10.0.0.52', type: 'Unauthorized Access', severity: 'Medium', status: 'Logged', time: '12 mins ago' }
    ];

    ngOnInit() {
        // Three.js initialization logic would go here
    }
}
