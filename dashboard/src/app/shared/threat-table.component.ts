import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
    selector: 'app-threat-table',
    standalone: true,
    imports: [CommonModule],
    template: `
    <div class="table-container">
      <table>
        <thead>
          <tr>
            <th>Source IP</th>
            <th>Type</th>
            <th>Severity</th>
            <th>Status</th>
            <th>Timestamp</th>
          </tr>
        </thead>
        <tbody>
          <tr *ngFor="let threat of threats">
            <td>{{ threat.ip }}</td>
            <td>{{ threat.type }}</td>
            <td>
              <span class="badge" [ngClass]="'badge-' + threat.severity.toLowerCase()">
                {{ threat.severity }}
              </span>
            </td>
            <td>{{ threat.status }}</td>
            <td>{{ threat.time }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  `,
    styles: [`
    .table-container { overflow-x: auto; }
    table { width: 100%; border-collapse: collapse; margin-top: 1rem; }
    th { text-align: left; padding: 1rem; border-bottom: 1px solid rgba(255,255,255,0.1); color: #888; }
    td { padding: 1rem; border-bottom: 1px solid rgba(255,255,255,0.05); }
    .badge { padding: 4px 8px; border-radius: 4px; font-size: 0.75rem; font-weight: bold; }
    .badge-critical { background: rgba(255, 0, 85, 0.2); color: #ff0055; border: 1px solid #ff0055; }
    .badge-high { background: rgba(255, 120, 0, 0.2); color: #ff7800; border: 1px solid #ff7800; }
    .badge-medium { background: rgba(0, 242, 255, 0.2); color: #00f2ff; border: 1px solid #00f2ff; }
  `]
})
export class ThreatTableComponent {
    @Input() threats: any[] = [];
}
