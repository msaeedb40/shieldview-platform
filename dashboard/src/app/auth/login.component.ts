import { Component, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { RouterLink } from '@angular/router';
import { AuthService } from './auth.service';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [CommonModule, FormsModule, RouterLink],
  template: `
    <div class="auth-wrapper">
      <div class="glass-panel auth-card">
        <h1>ShieldView</h1>
        <p class="subtitle">Secure Proactive Platform</p>
        
        <form (submit)="onSubmit($event)">
          <input type="text" name="username" [(ngModel)]="credentials.username" placeholder="Username" required>
          <input type="password" name="password" [(ngModel)]="credentials.password" placeholder="Password" required>
          
          <button type="submit" class="btn-primary w-full" [disabled]="loading">
            {{ loading ? 'SIGNING IN...' : 'SIGN IN' }}
          </button>
        </form>
        
        <div class="auth-footer">
          <p><a routerLink="/forgot-password">Forgot Password?</a></p>
          <span>Don't have an account?</span>
          <a routerLink="/register">Register</a>
        </div>
      </div>
    </div>
  `,
  styles: [`
    .auth-wrapper {
      height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      background: radial-gradient(circle at top right, #1a1a1a, #050505);
    }
    .auth-card { width: 400px; text-align: center; }
    h1 {
      margin: 0;
      font-size: 2.5rem;
      background: linear-gradient(45deg, #00f2ff, #7000ff);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }
    .subtitle { color: #888; margin-bottom: 2rem; }
    .auth-footer { margin-top: 1.5rem; font-size: 0.9rem; color: #aaa; }
    .auth-footer a { color: #00f2ff; text-decoration: none; margin-left: 0.5rem; }
    .auth-footer p { margin-bottom: 0.5rem; }
    .w-full { width: 100%; }
  `]
})
export class LoginComponent {
  private authService = inject(AuthService);
  credentials = { username: '', password: '' };
  loading = false;

  onSubmit(e: Event) {
    e.preventDefault();
    this.loading = true;
    this.authService.login(this.credentials).subscribe({
      next: () => this.loading = false,
      error: () => {
        alert("Login failed. Please check credentials.");
        this.loading = false;
      }
    });
  }
}
