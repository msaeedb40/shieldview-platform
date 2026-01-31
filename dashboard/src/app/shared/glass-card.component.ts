import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
    selector: 'app-glass-card',
    standalone: true,
    imports: [CommonModule],
    template: `
    <div class="glass-panel card-content">
      <div class="card-header" *ngIf="title">
        <h3>{{ title }}</h3>
      </div>
      <ng-content></ng-content>
    </div>
  `,
    styles: [`
    .card-content {
      height: 100%;
      padding: 1.5rem;
    }
    .card-header h3 {
      margin: 0 0 1rem 0;
      font-size: 1.1rem;
      color: #888;
      text-transform: uppercase;
      letter-spacing: 1px;
    }
  `]
})
export class GlassCardComponent {
    @Input() title?: string;
}
