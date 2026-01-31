import { Component, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { RouterLink } from '@angular/router';
import { AuthService } from './auth.service';

@Component({
    selector: 'app-forgot-password',
    standalone: true,
    imports: [CommonModule, FormsModule, RouterLink],
    template: `
    <div class="auth-wrapper">
      <div class="glass-panel auth-card">
        <h1>Reset Access</h1>
        <p class="subtitle">Enter your email to receive a recovery link</p>
        
        <form (submit)="onSubmit($event)">
          <input type="email" name="email" [(ngModel)]="email" placeholder="Email Address" required>
          <button type="submit" class="btn-primary w-full" [disabled]="loading">
            {{ loading ? 'SENDING...' : 'SEND RESET LINK' }}
          </button>
        </form>

        <div *ngIf="message" class="success-msg">{{ message }}</div>
        
        <div class="auth-footer">
          <span>Remember your password?</span>
          <a routerLink="/login">Sign In</a>
        </div>
      </div>
    </div>
  `,
    styles: [`
    .success-msg { color: #00f2ff; margin-top: 1rem; font-size: 0.9rem; }
  `]
})
export class ForgotPasswordComponent {
    private authService = inject(AuthService);
    email = '';
    loading = false;
    message = '';

    onSubmit(e: Event) {
        e.preventDefault();
        this.loading = true;
        this.authService.requestPasswordReset(this.email).subscribe({
            next: (res) => {
                this.message = res.message;
                this.loading = false;
            },
            error: () => this.loading = false
        });
    }
}
